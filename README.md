# Agentic Resume Tailoring App

This project turns a pasted job description into a tailored LaTeX resume by running a Codex-powered resume workflow over the experience files in `experiences/`.

Use it in either mode:

- CLI workflow: paste a job description into `job_description.txt`, then run `python agentic_resume.py`.
- Local web studio: run `python resume_workflow_server.py`, then open `http://127.0.0.1:8765`.

## Fast Start With Codex

After cloning the project, open the folder in Codex and paste this:

```text
Set up this resume app from scratch and run it.

Please:
1. Inspect the repo.
2. Check whether Python 3.11+ is available.
3. Create a virtual environment if one does not exist.
4. Activate the virtual environment.
5. Confirm there are no Python package dependencies to install, or install any dependencies if the repo later adds a requirements file.
6. Confirm the Codex CLI is installed and authenticated because agentic_resume.py shells out to the `codex` command.
7. Confirm whether `pdflatex` is installed. If it is missing, run the app without PDF compilation and tell me how to install MiKTeX or TeX Live later.
8. Run the local workflow studio with `python resume_workflow_server.py`.
9. Give me the local URL and keep the server running.
```

The app has no current third-party Python package dependencies. It uses the Python standard library, local JSON files, and the external `codex` command.

## Manual Setup

Clone and enter the project:

```powershell
git clone <repo-url>
cd resapp
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Check Python:

```powershell
python --version
```

Required external tools:

- Codex CLI: required for the agent workflow because `agentic_resume.py` calls `codex`.
- `pdflatex`: optional, only needed when compiling a PDF.

Check them:

```powershell
codex --version
pdflatex --version
```

If `pdflatex` is missing, you can still generate the final `.tex` resume. Install MiKTeX or TeX Live later if you want PDF output.

## Run The Web Studio

Start the local UI:

```powershell
python resume_workflow_server.py
```

Open:

```text
http://127.0.0.1:8765
```

In the studio you can:

- Paste a job description.
- Generate a tailored resume.
- Review generated LaTeX/PDF files.
- Submit feedback.
- Regenerate the final resume.

Generated UI runs are saved under:

```text
outputs/agentic_ui/
```

## Run The CLI Workflow

Paste the job description into:

```text
job_description.txt
```

Run:

```powershell
python agentic_resume.py
```

Final LaTeX output:

```text
outputs/agentic/latest/04_final_resume.tex
```

To also compile a PDF:

```powershell
python agentic_resume.py --compile-pdf
```

PDF compilation requires `pdflatex`.

## Common Commands

Use a different job description file:

```powershell
python agentic_resume.py --jd path\to\job_description.txt
```

Use a different output folder:

```powershell
python agentic_resume.py --output-dir outputs/agentic/my_application
```

Choose a Codex model:

```powershell
python agentic_resume.py --model gpt-5
```

Keep existing output folder contents:

```powershell
python agentic_resume.py --no-clean
```

Set a run date folder:

```powershell
python agentic_resume.py --run-date 2026-07-14
```

## Feedback Loop

After a resume is generated, revise it with feedback:

```powershell
python agentic_resume.py `
  --resume-dir outputs\agentic\latest `
  --feedback "Make the bullets more natural and reduce repeated operations language."
```

For longer feedback:

```powershell
notepad feedback.txt
python agentic_resume.py `
  --resume-dir outputs\agentic\latest `
  --feedback-file feedback.txt
```

Feedback updates these files in the selected output folder:

```text
03_resume_content.json
04_final_resume.tex
04_final_resume.pdf
05_rule_check.json
feedback_latest.txt
```

## How The Agent Pipeline Works

The workflow runs these stages:

1. JD intelligence: extracts role title, company context, responsibilities, competencies, tools, keywords, reusable JD phrases, evidence needs, and claims to avoid.
2. Evidence mapping: reads `experiences/*.json` and maps the job requirements to truthful resume evidence.
3. Resume writing: creates the summary, experience bullets, skills, and alignment notes.
4. LaTeX build: renders the structured resume into `04_final_resume.tex`.
5. QA: checks honesty, alignment, bullet counts, summary length, unsupported claims, and LaTeX risks.

Generated CLI files are saved under:

```text
outputs/agentic/latest/
  input_job_description.txt
  01_jd_profile.json
  02_selected_evidence.json
  02b_evidence_rationale.md
  03_resume_content.json
  04_final_resume.tex
  04_final_resume.pdf
  05_rule_check.json
  prompts/
  raw/
  logs/
```

The `prompts/`, `raw/`, and `logs/` folders make each agent run inspectable.

## Project Structure

```text
agentic_resume.py          Main CLI workflow
resume_workflow_server.py  Local web studio server
workflow_web/              Browser UI assets
experiences/               Source experience JSON files
job_description.txt        Default input job description
outputs/                   Generated resumes and run artifacts
resume_matcher.py          Legacy deterministic matcher
```

## Troubleshooting

`codex` is not recognized:

Install and authenticate the Codex CLI, then reopen the terminal and run `codex --version`.

`pdflatex was not found`:

Run without `--compile-pdf`, or install MiKTeX/TeX Live and retry with `--compile-pdf`.

PowerShell will not activate `.venv`:

Run PowerShell as your user and allow local scripts for the current user:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Port `8765` is already in use:

```powershell
python resume_workflow_server.py --port 8766
```

Then open:

```text
http://127.0.0.1:8766
```

## Legacy

`resume_matcher.py` is kept for deterministic debugging and comparison. The main workflow is `agentic_resume.py`.
