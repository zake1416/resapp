#!/usr/bin/env python3
"""Local workflow UI for the agentic resume generator."""

from __future__ import annotations

import argparse
import json
import mimetypes
import threading
import traceback
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse

import agentic_resume


ROOT = Path(__file__).resolve().parent
WEB_ROOT = ROOT / "workflow_web"
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765

jobs: dict[str, dict] = {}
jobs_lock = threading.Lock()


def safe_resolve(path: str | Path) -> Path:
    resolved = (ROOT / path).resolve() if not Path(path).is_absolute() else Path(path).resolve()
    if resolved != ROOT and ROOT not in resolved.parents:
        raise ValueError(f"Path is outside workspace: {path}")
    return resolved


def json_response(handler: BaseHTTPRequestHandler, status: int, payload: dict) -> None:
    body = json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def read_json(handler: BaseHTTPRequestHandler) -> dict:
    length = int(handler.headers.get("Content-Length", "0") or "0")
    raw = handler.rfile.read(length).decode("utf-8") if length else "{}"
    return json.loads(raw or "{}")


def relative(path: Path | None) -> str | None:
    if not path:
        return None
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def public_job(job: dict) -> dict:
    payload = dict(job)
    payload.pop("thread", None)
    return payload


def set_job(job_id: str, **updates) -> None:
    with jobs_lock:
        jobs[job_id].update(updates)


def get_job(job_id: str) -> dict | None:
    with jobs_lock:
        job = jobs.get(job_id)
        return public_job(job) if job else None


def collect_files(output_dir: Path | None) -> dict[str, str]:
    if not output_dir:
        return {}
    files = {}
    for label, name in {
        "tex": "04_final_resume.tex",
        "pdf": "04_final_resume.pdf",
        "content": "03_resume_content.json",
        "rules": "05_rule_check.json",
        "evidence": "02b_evidence_rationale.md",
        "feedback": "feedback_latest.txt",
        "compile_log": "latex_compile.log",
    }.items():
        path = output_dir / name
        if path.exists():
            files[label] = relative(path) or str(path)
    return files


def run_generation(job_id: str, payload: dict) -> None:
    try:
        jd_text = str(payload.get("job_description", "")).strip()
        if not jd_text:
            raise ValueError("Paste a job description before running the workflow.")
        jd_path = ROOT / "outputs" / "workflow_inputs" / f"{job_id}_job_description.txt"
        agentic_resume.write_text(jd_path, jd_text)
        args = SimpleNamespace(
            jd=str(jd_path),
            experiences=str(ROOT / "experiences"),
            output_dir=str(ROOT / "outputs" / "agentic_ui"),
            model=payload.get("model") or None,
            revision_attempts=int(payload.get("revision_attempts") or 2),
            no_clean=False,
            run_date=None,
            compile_pdf=bool(payload.get("compile_pdf", True)),
        )
        set_job(job_id, status="running", stage="generate", message="Generating tailored resume...")
        results = agentic_resume.run_pipeline(args)
        output_dir = Path(args.resolved_output_dir)
        set_job(
            job_id,
            status="done",
            stage="review",
            message="Resume generated. Review it, then submit feedback if needed.",
            output_dir=relative(output_dir),
            files=collect_files(output_dir),
            steps=["JD captured", "Evidence selected", "Resume written", "LaTeX rendered", "PDF compiled"],
            agents=[result.name for result in results],
        )
    except Exception as exc:
        set_job(
            job_id,
            status="error",
            stage="error",
            message=str(exc),
            error=traceback.format_exc(),
        )


def run_feedback(job_id: str, payload: dict) -> None:
    try:
        feedback = str(payload.get("feedback", "")).strip()
        if not feedback:
            raise ValueError("Paste feedback before running the feedback revision.")
        with jobs_lock:
            job = jobs[job_id]
            output_dir_text = job.get("output_dir")
        if not output_dir_text:
            raise ValueError("Generate a resume before submitting feedback.")
        output_dir = safe_resolve(output_dir_text)
        args = SimpleNamespace(
            resume_dir=str(output_dir),
            feedback=feedback,
            feedback_file=None,
            model=payload.get("model") or None,
            revision_attempts=int(payload.get("revision_attempts") or 2),
        )
        set_job(job_id, status="running", stage="feedback", message="Applying feedback and regenerating final files...")
        results = agentic_resume.run_feedback_revision(args)
        set_job(
            job_id,
            status="done",
            stage="final",
            message="Feedback applied. Final LaTeX and PDF are ready.",
            output_dir=relative(output_dir),
            files=collect_files(output_dir),
            steps=["Feedback captured", "Resume revised", "Rules checked", "LaTeX rendered", "PDF compiled"],
            agents=[result.name for result in results],
        )
    except Exception as exc:
        set_job(
            job_id,
            status="error",
            stage="error",
            message=str(exc),
            error=traceback.format_exc(),
        )


class WorkflowHandler(BaseHTTPRequestHandler):
    server_version = "ResumeWorkflow/0.1"

    def log_message(self, fmt: str, *args) -> None:
        return

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/jobs":
            with jobs_lock:
                payload = {"jobs": [public_job(job) for job in jobs.values()]}
            json_response(self, 200, payload)
            return
        if parsed.path.startswith("/api/jobs/"):
            job_id = parsed.path.rsplit("/", 1)[-1]
            job = get_job(job_id)
            if not job:
                json_response(self, 404, {"error": "Job not found"})
                return
            json_response(self, 200, job)
            return
        if parsed.path == "/api/file":
            params = parse_qs(parsed.query)
            target = params.get("path", [""])[0]
            try:
                file_path = safe_resolve(target)
                if not file_path.exists() or not file_path.is_file():
                    raise FileNotFoundError(target)
                ctype = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
                data = file_path.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", ctype)
                if ctype == "application/pdf":
                    self.send_header("Content-Disposition", f'inline; filename="{file_path.name}"')
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            except Exception as exc:
                json_response(self, 404, {"error": str(exc)})
            return
        self.serve_static(parsed.path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        try:
            if parsed.path == "/api/jobs":
                payload = read_json(self)
                job_id = uuid.uuid4().hex[:12]
                job = {
                    "id": job_id,
                    "status": "queued",
                    "stage": "queued",
                    "message": "Queued",
                    "output_dir": None,
                    "files": {},
                    "steps": [],
                    "agents": [],
                }
                thread = threading.Thread(target=run_generation, args=(job_id, payload), daemon=True)
                job["thread"] = thread
                with jobs_lock:
                    jobs[job_id] = job
                thread.start()
                json_response(self, 202, public_job(job))
                return
            if parsed.path.startswith("/api/jobs/") and parsed.path.endswith("/feedback"):
                job_id = parsed.path.split("/")[-2]
                with jobs_lock:
                    if job_id not in jobs:
                        json_response(self, 404, {"error": "Job not found"})
                        return
                payload = read_json(self)
                thread = threading.Thread(target=run_feedback, args=(job_id, payload), daemon=True)
                with jobs_lock:
                    jobs[job_id]["thread"] = thread
                thread.start()
                json_response(self, 202, get_job(job_id) or {})
                return
            json_response(self, 404, {"error": "Unknown endpoint"})
        except Exception as exc:
            json_response(self, 400, {"error": str(exc)})

    def serve_static(self, request_path: str) -> None:
        if request_path in {"", "/"}:
            request_path = "/index.html"
        try:
            file_path = safe_resolve(WEB_ROOT / request_path.lstrip("/"))
            if not file_path.exists() or not file_path.is_file():
                raise FileNotFoundError(request_path)
            ctype = mimetypes.guess_type(str(file_path))[0] or "text/plain"
            data = file_path.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        except Exception:
            json_response(self, 404, {"error": "Not found"})


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the local resume workflow studio.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), WorkflowHandler)
    print(f"Resume Workflow Studio running at http://{args.host}:{args.port}")
    server.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
