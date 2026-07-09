
#!/usr/bin/env python3
"""Simple JD-to-resume matcher and LaTeX builder.

Flow:
1. Analyze job_description.txt into competencies, tools, keywords, and JD phrases.
2. Score every point in experiences/*.json against that profile.
3. Select the strongest evidence per experience.
4. Ask Codex once to rewrite selected evidence into resume bullets.
5. Render deterministic LaTeX with no placeholders and no projects.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_DIR = Path("outputs/agentic")

EXPERIENCES = [
    {
        "key": "salesforce",
        "file": "salesforce.json",
        "company": "Salesforce",
        "location": "USA",
        "title": "Finance Operations, Governance & AI Enablement Analyst",
        "dates": "Apr 2025 -- March 2026",
        "count": 6,
        "jd_first_slots": 2,
    },
    {
        "key": "marketmaker_pm",
        "file": "mmrcePM.json",
        "company": "Market Maker CRE",
        "location": "USA",
        "title": "Financial Modeling & Strategic Operations Analyst",
        "dates": "Jan 2025 -- Apr 2025",
        "count": 3,
        "jd_first_slots": 2,
    },
    {
        "key": "marketmaker_ba",
        "file": "mmrceBA.json",
        "company": "Market Maker CRE",
        "location": "USA",
        "title": "Business Analysis & Financial Data Analyst",
        "dates": "Aug 2024 -- Dec 2024",
        "count": 3,
        "jd_first_slots": 1,
        "continuation": True,
    },
    {
        "key": "vista",
        "file": "vista.json",
        "company": "Vista Research Services",
        "location": "USA",
        "title": "Analytics, Risk & Automation Analyst",
        "dates": "May 2024 -- Apr 2025",
        "count": 4,
        "jd_first_slots": 1,
    },
    {
        "key": "ltimindtree",
        "file": "lti.json",
        "company": "LTIMindtree",
        "location": "India",
        "title": "Data Quality, BI & Systems Analyst",
        "dates": "Aug 2021 -- Aug 2023",
        "count": 4,
        "jd_first_slots": 1,
    },
]

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "in", "into",
    "is", "it", "of", "on", "or", "our", "that", "the", "their", "this", "to", "with",
    "you", "your", "we", "will", "work", "role", "team", "teams", "experience", "support",
    "across", "using", "including", "through", "within", "about", "job", "description",
}

TOOL_HINTS = [
    "HubSpot", "ServiceNow", "Azure DevOps", "Power BI", "Tableau", "JIRA", "SharePoint", "Salesforce",
    "SQL", "Python", "Streamlit", "Excel", "Azure", "Copilot", "AI agents", "copilots",
    "ZoomInfo", "Cvent", "Google Analytics", "GA4", "Monday.com", "ON24", "SAP",
    "low-code", "no-code", "workflow automation", "CRM", "Agile", "Lean", "SAFe", "PMP",
]

COMPETENCY_PATTERNS = {
    "Tool Integration & Flow": ["connect", "integration", "tools", "serviceNow", "azure devops", "power bi", "single view", "visibility"],
    "Workflow Improvement": ["workflow", "manual effort", "duplication", "simplify", "process", "intake", "delivery"],
    "Portfolio Governance": ["prioritization", "sequencing", "governance", "dependencies", "risks", "progress", "roadmap"],
    "AI & Automation": ["ai", "automation", "agents", "copilots", "ai-driven", "automated"],
    "Enablement & Adoption": ["adoption", "training", "templates", "job aids", "coach", "self-service"],
    "Stakeholder Partnership": ["stakeholder", "partner", "product", "pmo", "technology", "communicate"],
    "Analytics & Reporting": ["dashboard", "reporting", "insights", "analysis", "metrics", "decision-making"],
    "Agile Delivery": ["agile", "sprint", "scrum", "backlog", "delivery", "execution tracking"],
}


@dataclass(frozen=True)
class AgentResult:
    name: str
    prompt_path: Path
    output_path: Path
    raw_path: Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, dict):
        return " ".join(clean_text(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(clean_text(v) for v in value)
    return str(value)


def tokens(text: str) -> list[str]:
    raw = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]*", text.lower())
    return [t.strip(".,;:!?()[]{}") for t in raw if t not in STOPWORDS and len(t) > 1]


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9$]+", text or ""))


def unique(values: list[str], limit: int | None = None) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for value in values:
        clean = re.sub(r"\s+", " ", str(value)).strip(" -?\t\r\n")
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            out.append(clean)
            if limit and len(out) >= limit:
                break
    return out


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return slug or "resume"


def extract_metrics(text: str) -> list[str]:
    patterns = [
        r"\$\d+(?:\.\d+)?\s?[KkMmBb]?",
        r"\b\d+(?:\.\d+)?%",
        r"\b\d+\+?\s?(?:projects|apps|applications|teams|stakeholders|workflows|dashboards|articles|cases|clients|users|reports|sprints|initiatives|pages|risks)\b",
        r"\b\d+\+?\b",
    ]
    found: list[str] = []
    for pattern in patterns:
        found.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    return unique(found, 8)


def extract_jd_phrases(jd_text: str) -> list[str]:
    phrases: list[str] = []
    for line in jd_text.splitlines():
        clean = re.sub(r"\s+", " ", line).strip(" -?\t")
        if 4 <= len(clean.split()) <= 18:
            lower = clean.lower()
            if any(k in lower for k in [
                "connect", "visibility", "reduce", "single view", "governance", "ai", "automation",
                "adoption", "training", "templates", "partner", "workflow", "dashboard", "intake", "delivery",
                "planning", "roadmaps", "execution", "dependencies", "risks", "progress",
            ]):
                phrases.append(clean)
    return unique(phrases, 35)


def analyze_jd(jd_text: str) -> dict[str, Any]:
    lower = jd_text.lower()
    required_tools = [tool for tool in TOOL_HINTS if tool.lower() in lower]
    competencies = []
    for comp, needles in COMPETENCY_PATTERNS.items():
        if any(needle.lower() in lower for needle in needles):
            competencies.append(comp)
    counts: dict[str, int] = {}
    for token in tokens(jd_text):
        counts[token] = counts.get(token, 0) + 1
    keywords = [word for word, _ in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:45]]
    phrases = extract_jd_phrases(jd_text)
    title = ""
    for line in jd_text.splitlines()[:20]:
        if re.search(r"analyst|manager|associate|specialist|consultant", line, re.IGNORECASE):
            title = line.strip(" -:")
            break
    company_name = ""
    for line in jd_text.splitlines()[:30]:
        m = re.search(r"about\s+([A-Za-z0-9&.'-]+)", line, re.IGNORECASE)
        if m:
            company_name = m.group(1).strip(" .-")
            break
    priority_phrases = unique([
        phrase for phrase in phrases
        if any(term in phrase.lower() for term in [
            "connect", "intake", "delivery", "visibility", "single view", "reduce duplication",
            "manual effort", "governance", "ai", "automation", "adoption", "planning", "roadmaps",
            "execution tracking", "dependencies", "risks", "progress",
        ])
    ], 12)
    return {
        "role_title": title,
        "company_name": company_name,
        "core_competencies": competencies,
        "required_tools_keywords": required_tools,
        "keywords": keywords,
        "responsibility_phrases": phrases,
        "priority_jd_responsibilities": priority_phrases,
        "metric_themes": ["visibility", "manual effort reduction", "tool adoption", "delivery acceleration", "workflow consistency"],
    }


def jd_blob(jd_profile: dict[str, Any]) -> str:
    return clean_text([
        jd_profile.get("role_title", ""),
        jd_profile.get("core_competencies", []),
        jd_profile.get("required_tools_keywords", []),
        jd_profile.get("keywords", []),
        jd_profile.get("responsibility_phrases", []),
        jd_profile.get("priority_jd_responsibilities", []),
    ]).lower()


def jd_has_any(jd_profile: dict[str, Any], terms: list[str]) -> bool:
    blob = jd_blob(jd_profile)
    return any(term in blob for term in terms)


def resolve_experience_title(config: dict[str, Any], jd_profile: dict[str, Any]) -> str:
    """Choose truthful, JD-aware functional titles instead of reusing one fixed title family."""
    key = config["key"]
    title_sets = [
        (
            [
                "valuation", "investment", "investments", "m&a", "acquisition", "divestiture",
                "project finance", "financial modeling", "profitability", "capital structure",
                "power purchase", "ppa", "solar", "storage", "renewable",
            ],
            {
                "salesforce": "Finance Operations, Governance & Risk Analyst",
                "marketmaker_pm": "Financial Modeling & Investment Analysis Analyst",
                "marketmaker_ba": "Business Analysis & Financial Data Analyst",
                "vista": "Analytics, Risk & Automation Analyst",
                "ltimindtree": "Data Quality, BI & Systems Analyst",
            },
        ),
        (
            ["contract", "contracts", "pricing", "deal", "deals", "revenue", "sales", "forecasting"],
            {
                "salesforce": "Revenue Operations, Governance & Controls Analyst",
                "marketmaker_pm": "Revenue Strategy & Financial Analysis Analyst",
                "marketmaker_ba": "Business Systems & Revenue Data Analyst",
                "vista": "Analytics, Automation & Operations Analyst",
                "ltimindtree": "BI, Data Quality & Systems Analyst",
            },
        ),
        (
            ["product", "roadmap", "backlog", "sprint", "agile", "pmo", "portfolio", "program"],
            {
                "salesforce": "Portfolio Governance & Process Improvement Analyst",
                "marketmaker_pm": "Product Operations & Program Analyst",
                "marketmaker_ba": "Business Systems & Product Analyst",
                "vista": "Product Analytics & Automation Analyst",
                "ltimindtree": "Agile Delivery, BI & Quality Analyst",
            },
        ),
        (
            ["ai", "automation", "copilot", "agents", "workflow automation", "digital transformation"],
            {
                "salesforce": "AI Enablement & Finance Operations Analyst",
                "marketmaker_pm": "Automation, Product & Operations Analyst",
                "marketmaker_ba": "Business Systems & Workflow Automation Analyst",
                "vista": "AI Product, Analytics & Automation Analyst",
                "ltimindtree": "Automation, BI & Quality Transformation Analyst",
            },
        ),
        (
            ["analytics", "reporting", "dashboard", "business intelligence", "sql", "tableau", "power bi", "metrics"],
            {
                "salesforce": "Finance Operations & Reporting Analyst",
                "marketmaker_pm": "Strategic Analytics & Operations Analyst",
                "marketmaker_ba": "Business Analysis & Data Insights Analyst",
                "vista": "Analytics & Automation Analyst",
                "ltimindtree": "BI, Data Quality & Systems Analyst",
            },
        ),
    ]
    for terms, titles in title_sets:
        if jd_has_any(jd_profile, terms):
            return titles.get(key, config["title"])
    return config["title"]

def load_experience_points(experience_dir: Path, config: dict[str, Any]) -> list[dict[str, Any]]:
    path = experience_dir / config["file"]
    if not path.exists():
        raise FileNotFoundError(f"Missing experience file: {path}")
    data = json.loads(read_text(path))
    points = data.get("points", [])
    normalized: list[dict[str, Any]] = []
    for point in points:
        tags = point.get("tags", {}) or {}
        searchable = clean_text([
            point.get("point_title"),
            point.get("base_resume_point"),
            tags.get("core_competency"),
            tags.get("functional_skill"),
            tags.get("business_outcome"),
            tags.get("evidence_proof"),
            tags.get("metric_placeholder"),
            tags.get("adaptation_direction"),
        ])
        normalized.append({
            "id": point.get("id", ""),
            "point_title": point.get("point_title", ""),
            "base_resume_point": point.get("base_resume_point", ""),
            "core_competency": tags.get("core_competency", []),
            "functional_skill": tags.get("functional_skill", []),
            "business_outcome": tags.get("business_outcome", []),
            "evidence_proof": tags.get("evidence_proof", []),
            "metrics": extract_metrics(clean_text(tags.get("metric_placeholder", [])) + " " + searchable),
            "adaptation_direction": tags.get("adaptation_direction", []),
            "searchable": searchable,
        })
    return normalized


def score_point(point: dict[str, Any], jd_profile: dict[str, Any]) -> dict[str, Any]:
    point_text = point["searchable"].lower()
    point_tokens = set(tokens(point_text))
    jd_tokens = set(jd_profile["keywords"])
    overlap = sorted(point_tokens & jd_tokens)
    score = len(overlap) * 1.5
    matched_competencies = []
    for comp in jd_profile["core_competencies"]:
        comp_tokens = set(tokens(comp))
        tag_tokens = set(tokens(clean_text([point.get("core_competency"), point.get("functional_skill"), point.get("adaptation_direction")])) )
        if comp_tokens & tag_tokens or any(t in point_text for t in comp_tokens):
            score += 8
            matched_competencies.append(comp)
    matched_phrases = []
    for phrase in jd_profile["responsibility_phrases"]:
        phrase_tokens = set(tokens(phrase))
        if len(phrase_tokens & point_tokens) >= max(1, min(3, len(phrase_tokens) // 2)):
            score += 4
            matched_phrases.append(phrase)
    matched_tools = []
    for tool in jd_profile["required_tools_keywords"]:
        if tool.lower() in point_text:
            score += 7
            matched_tools.append(tool)
    if point["metrics"]:
        score += 3
    if point.get("evidence_proof"):
        score += 2
    return {
        "score": round(score, 2),
        "matched_keywords": overlap[:20],
        "matched_core_competencies": unique(matched_competencies, 8),
        "matched_jd_phrases": unique(matched_phrases, 8),
        "matched_tools": unique(matched_tools, 8),
    }


def select_evidence(jd_profile: dict[str, Any], experience_dir: Path) -> dict[str, Any]:
    selected: list[dict[str, Any]] = []
    for config in EXPERIENCES:
        scored = []
        for point in load_experience_points(experience_dir, config):
            score = score_point(point, jd_profile)
            scored.append({**point, **score})
        scored.sort(key=lambda p: p["score"], reverse=True)
        chosen = scored[: config["count"]]
        selected.append({
            "key": config["key"],
            "company": config["company"],
            "title": resolve_experience_title(config, jd_profile),
            "target_count": config["count"],
            "jd_first_slots": config.get("jd_first_slots", 0),
            "priority_jd_responsibilities": jd_profile.get("priority_jd_responsibilities", []),
            "selected_points": [
                {k: v for k, v in point.items() if k != "searchable"}
                for point in chosen
            ],
        })
    return {"experiences": selected}



def selected_evidence_text(selected_evidence: dict[str, Any]) -> str:
    return clean_text(selected_evidence).lower()


def unsupported_jd_tools(jd_profile: dict[str, Any], selected_evidence: dict[str, Any]) -> list[str]:
    evidence = selected_evidence_text(selected_evidence)
    unsupported: list[str] = []
    for tool in jd_profile.get("required_tools_keywords", []):
        key = tool.lower()
        if key in {"crm", "workflow automation", "low-code", "no-code", "agile", "lean"}:
            continue
        if key not in evidence:
            unsupported.append(tool)
    return unique(unsupported)


def unsupported_claims(content: dict[str, Any], unsupported_tools: list[str]) -> list[str]:
    resume_text = clean_text(content).lower()
    claims = []
    for tool in unsupported_tools:
        if tool.lower() in resume_text:
            claims.append(tool)
    return claims


def codex_path() -> str | None:
    found = shutil.which("codex")
    if found:
        return found
    candidates = [
        Path.home() / "AppData" / "Local" / "Programs" / "OpenAI" / "Codex" / "bin" / "codex.exe",
        Path.home() / "AppData" / "Local" / "Programs" / "OpenAI" / "Codex" / "codex.exe",
    ]
    for candidate in candidates:
        if candidate.exists():
            return str(candidate)
    return None


def extract_json(text: str) -> Any:
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        text = fenced.group(1)
    start = min([i for i in [text.find("{"), text.find("[")] if i != -1], default=-1)
    if start == -1:
        raise ValueError("Codex output did not contain JSON")
    obj, _ = json.JSONDecoder().raw_decode(text[start:].strip())
    return obj


def run_codex_json(name: str, prompt: str, output_path: Path, output_dir: Path, model: str | None) -> AgentResult:
    resolved = codex_path()
    if not resolved:
        raise RuntimeError(
            "Codex CLI was not found. Expected Windows path: "
            r"%LOCALAPPDATA%\Programs\OpenAI\Codex\bin\codex.exe"
        )
    prompt_path = output_dir / "prompts" / f"{name}.md"
    raw_path = output_dir / "raw" / f"{name}.txt"
    write_text(prompt_path, prompt)
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        resolved,
        "exec",
        "--skip-git-repo-check",
        "--sandbox",
        "danger-full-access",
        "-C",
        str(Path.cwd()),
        "-o",
        str(raw_path),
    ]
    if model:
        command.extend(["--model", model])
    command.append("-")
    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    log = "\n".join(["STDOUT:", completed.stdout, "STDERR:", completed.stderr])
    write_text(output_dir / "logs" / f"{name}.log", log)
    if completed.returncode != 0:
        raise RuntimeError(f"Codex step failed: {name}. See {output_dir / 'logs' / f'{name}.log'}")
    raw = read_text(raw_path)
    data = extract_json(raw)
    write_text(output_path, json.dumps(data, indent=2, ensure_ascii=False))
    return AgentResult(name, prompt_path, output_path, raw_path)


def writer_prompt(jd_profile: dict[str, Any], selected_evidence: dict[str, Any]) -> str:
    return f"""
You are writing a tailored resume from already-selected evidence. Keep it simple and high quality.

Goal:
- Use the job description's responsibilities, keywords, tools, and core competencies.
- Use only the selected truthful evidence from the candidate JSONs.
- Rewrite each selected point into a strong resume bullet.

Bullet formula:
Strong action verb + JD-aligned impact + quantification/metric when available + business result.

Length rules:
- Alternate bullets within each experience: 15 words, 28 words, 15 words, 28 words, 15 words, 28 words.
- Acceptable ranges: short bullets 13-18 words; long bullets 24-30 words.
- Do not break grammar to hit the count.

Required bullet counts:
- Salesforce: 6
- Market Maker CRE Financial Modeling & Strategic Operations Analyst: 3
- Market Maker CRE Business Analysis & Financial Data Analyst: 3
- Vista Research Services: 4
- LTIMindtree: 4

JD-direct bullet rules:
- Salesforce bullets 1 and 2 must be built directly from the most important JD responsibilities, then backed by Salesforce evidence.
- Market Maker CRE PM bullets 1 and 2 must be built directly from the most important JD responsibilities, then backed by MarketMaker PM evidence.
- MarketMaker BA, Vista, and LTIMindtree bullet 1 must be built directly from the most important JD responsibility, then backed by that experience's evidence.
- "Direct from JD" means start with the JD responsibility/competency as the sentence idea, then attach truthful evidence and metrics. Do not start those bullets from the old base resume wording.
- For direct JD bullets, mirror responsibility intent like connect tools/data/workflows, lead-to-revenue process, CRM automation, lifecycle stages, member/customer journeys, campaign operations, reporting, clean data, reduce delays, handoffs, governance, AI automation, adoption, dashboards, planning, roadmaps, execution tracking, dependencies, risks, and progress.
- Do not write phrases like "Led HubSpot Automation" unless selected evidence explicitly proves HubSpot. Use "strengthened CRM automation workflows" or "improved lead-management operating cadence" instead.

Strict rules:
- Summary must be 45 words or fewer and use JD language.
- No Projects section.
- No placeholders.
- Do not claim direct ownership/use of JD tools unless selected evidence explicitly proves that tool. This includes HubSpot, ServiceNow, Power BI, ZoomInfo, Cvent, GA4, Monday.com, ON24, SAP, location, W2, visa, or certifications.
- If a priority JD responsibility contains an unsupported tool such as HubSpot, translate it truthfully into transferable language: CRM automation, lead-management workflows, lifecycle-stage governance, audience/list logic, reporting, data quality, handoffs, integrations, and revenue operations.
- You may use transferable language such as dashboards, reporting, workflow automation, intake-to-delivery visibility, tool adoption, governance, CRM processes, lifecycle stages, lead routing, and execution tracking when evidence supports it.
- Prefer real metrics from evidence: percentages, dollar values, counts, teams, workflows, projects, articles, apps.
- Every bullet should visibly connect to at least one JD responsibility or core competency.
- Job titles in the LaTeX are intentionally functional/JD-aligned titles reflecting actual work, not necessarily HR-paper titles.

Return ONLY valid JSON with this exact shape:
{{
  "summary": "",
  "experiences": [
    {{"key": "salesforce", "bullets": []}},
    {{"key": "marketmaker_pm", "bullets": []}},
    {{"key": "marketmaker_ba", "bullets": []}},
    {{"key": "vista", "bullets": []}},
    {{"key": "ltimindtree", "bullets": []}}
  ],
  "skills": {{
    "Enterprise AI & Automation": [],
    "Systems, Workflow & Governance": [],
    "Analytics & Reporting": [],
    "Product, PMO & Stakeholder Operations": [],
    "Tools": []
  }}
}}

JD PROFILE:
{json.dumps(jd_profile, indent=2, ensure_ascii=False)}

SELECTED EVIDENCE:
{json.dumps(selected_evidence, indent=2, ensure_ascii=False)}
"""


def revision_prompt(jd_profile: dict[str, Any], selected_evidence: dict[str, Any], resume_content: dict[str, Any], rule_check: dict[str, Any]) -> str:
    return f"""
Revise this resume JSON to fix the validation issues. Return ONLY valid JSON in the same shape.

Keep the same selected evidence. Do not invent claims. Preserve strong JD alignment.
Short bullets must be 13-18 words. Long bullets must be 24-30 words.
Required counts must be exact. Summary must be 45 words or fewer.
Preserve the JD-direct bullet rules: Salesforce first 2, MarketMaker PM first 2, and first bullet for all remaining experiences must start from priority JD responsibilities.
Remove any unsupported direct tool claims flagged in validation. If HubSpot or another JD tool is unsupported by selected evidence, convert it to truthful transferable language such as CRM automation, lead routing, lifecycle workflows, reporting, data quality, integrations, or revenue operations.

VALIDATION ISSUES:
{json.dumps(rule_check, indent=2, ensure_ascii=False)}

JD PROFILE:
{json.dumps(jd_profile, indent=2, ensure_ascii=False)}

SELECTED EVIDENCE:
{json.dumps(selected_evidence, indent=2, ensure_ascii=False)}

CURRENT RESUME JSON:
{json.dumps(resume_content, indent=2, ensure_ascii=False)}
"""


def normalize_resume_content(content: dict[str, Any], jd_profile: dict[str, Any]) -> dict[str, Any]:
    by_key = {str(exp.get("key", "")): exp for exp in content.get("experiences", [])}
    experiences = []
    for config in EXPERIENCES:
        bullets = list(by_key.get(config["key"], {}).get("bullets", []) or [])[: config["count"]]
        experiences.append({
            "key": config["key"],
            "company": config["company"],
            "location": config["location"],
            "title": resolve_experience_title(config, jd_profile),
            "dates": config["dates"],
            "continuation": bool(config.get("continuation")),
            "bullets": bullets,
        })
    skills = content.get("skills") or {}
    return {
        "summary": str(content.get("summary", "")).strip(),
        "experiences": experiences,
        "skills": skills,
    }


def validate(content: dict[str, Any], unsupported_tools: list[str] | None = None) -> dict[str, Any]:
    issues: list[str] = []
    summary_words = word_count(content.get("summary", ""))
    if summary_words > 45:
        issues.append(f"Summary has {summary_words} words; maximum is 45.")
    counts: dict[str, int] = {}
    word_counts: dict[str, list[int]] = {}
    unsupported_tools = unsupported_tools or []
    direct_claims = unsupported_claims(content, unsupported_tools)
    for claim in direct_claims:
        issues.append(f"Unsupported direct tool claim: {claim}.")
    for config, exp in zip(EXPERIENCES, content.get("experiences", [])):
        bullets = exp.get("bullets", []) or []
        counts[config["key"]] = len(bullets)
        word_counts[config["key"]] = [word_count(b) for b in bullets]
        if len(bullets) != config["count"]:
            issues.append(f"{config['key']} has {len(bullets)} bullets; required {config['count']}.")
        for index, wc in enumerate(word_counts[config["key"]]):
            is_short = index % 2 == 0
            low, high, target = (13, 18, 15) if is_short else (24, 30, 28)
            if not low <= wc <= high:
                issues.append(f"{config['key']} bullet {index + 1} has {wc} words; target is {target}.")
    return {
        "status": "pass" if not issues else "needs_review",
        "summary_word_count": summary_words,
        "bullet_counts": counts,
        "bullet_word_counts": word_counts,
        "issues": issues,
    }


def latex_escape(text: Any) -> str:
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in str(text))


def render_items(bullets: list[str]) -> list[str]:
    return [f"\\resumeItem{{{latex_escape(bullet)}}}" for bullet in bullets]


def render_latex(content: dict[str, Any]) -> str:
    skills = content.get("skills", {}) or {}

    def skill_line(label: str) -> str:
        values = skills.get(label, []) or []
        return f"    \\textbf{{{latex_escape(label)}:}} {latex_escape(', '.join(map(str, values)))} \\\\"

    lines = [
        r"\documentclass[letterpaper,10pt]{article}",
        r"\usepackage{latexsym}",
        r"\usepackage[empty]{fullpage}",
        r"\usepackage{titlesec}",
        r"\usepackage{marvosym}",
        r"\usepackage[usenames,dvipsnames]{color}",
        r"\usepackage{verbatim}",
        r"\usepackage{enumitem}",
        r"\usepackage[hidelinks]{hyperref}",
        r"\usepackage{fancyhdr}",
        r"\usepackage[english]{babel}",
        r"\usepackage{tabularx}",
        r"\usepackage{fontawesome5}",
        r"\usepackage{multicol}",
        r"\setlength{\multicolsep}{-3.0pt}",
        r"\setlength{\columnsep}{-1pt}",
        r"\input{glyphtounicode}",
        "",
        r"\pagestyle{fancy}",
        r"\fancyhf{}",
        r"\renewcommand{\headrulewidth}{0pt}",
        r"\renewcommand{\footrulewidth}{0pt}",
        r"\addtolength{\oddsidemargin}{-0.6in}",
        r"\addtolength{\evensidemargin}{-0.5in}",
        r"\addtolength{\textwidth}{1.19in}",
        r"\addtolength{\topmargin}{-.7in}",
        r"\addtolength{\textheight}{1.4in}",
        r"\raggedbottom",
        r"\raggedright",
        r"\setlength{\tabcolsep}{0in}",
        r"\pdfgentounicode=1",
        "",
        r"\newcommand{\resumeItem}[1]{\item \small{#1}}",
        r"\newcommand{\resumeSubheading}[4]{",
        r"  \vspace{1pt}\item",
        r"    \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}",
        r"      \textbf{#1} & \textbf{\small #2} \\",
        r"      \textit{\small #3} & \textit{\small #4} \\",
        r"    \end{tabular*}\vspace{-6pt}",
        r"}",
        r"\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}",
        r"\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}",
        r"\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.15in, itemsep=1pt, topsep=3pt]}",
        r"\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-2pt}}",
        r"\renewcommand\labelitemi{\textbullet}",
        r"\renewcommand\labelitemii{\textbullet}",
        r"\titleformat{\section}{\vspace{-4pt}\scshape\raggedright\large\bfseries\color{MidnightBlue}}{}{0em}{}[\color{MidnightBlue}\titlerule \vspace{-5pt}]",
        "",
        r"\begin{document}",
        "",
        r"\begin{center}",
        r"    {\Huge \scshape Aishwarya Chourasia} \\ \vspace{1pt}",
        r"    \small \raisebox{-0.1\height}\faPhone\ +1 217-607-7336 ~ ",
        r"    \href{mailto:aishwarya7uiuc@gmail.com}{\raisebox{-0.2\height}\faEnvelope\ aishwarya7uiuc@gmail.com} ~ ",
        r"    \href{https://linkedin.com/in/aishwarya-chourasia-65b381151/}{\raisebox{-0.2\height}\faLinkedin\ LinkedIn} ~",
        r"    \href{https://aishwarya2510.github.io/portfolio_new/}{\raisebox{-0.2\height}\faBriefcase\ Portfolio}",
        r"\end{center}",
        "",
        r"\section{Summary}",
        r" \begin{itemize}[leftmargin=0.0in, label={}]",
        f"   \\item \\small{{{latex_escape(content.get('summary', ''))}}}",
        r" \end{itemize}",
        r"\vspace{-10pt}",
        r"\section{Experience}",
        r"  \resumeSubHeadingListStart",
        "",
    ]
    for exp in content.get("experiences", []):
        company = "" if exp.get("continuation") else exp["company"]
        location = "" if exp.get("continuation") else exp["location"]
        lines.extend([
            r"\resumeSubheading",
            f"{{{latex_escape(company)}}}{{{latex_escape(location)}}}",
            f"{{{latex_escape(exp['title'])}}}{{{latex_escape(exp['dates'])}}}",
            r"\resumeItemListStart",
            *render_items(exp.get("bullets", [])),
            r"\resumeItemListEnd",
            "",
            r"\vspace{-2pt}",
            "",
        ])
    lines.extend([
        r"\resumeSubHeadingListEnd",
        r"\vspace{-10pt}",
        r"\section{Skills}",
        r"\begin{itemize}[leftmargin=0.0in, label={}]",
        r"    \small{\item{",
        skill_line("Enterprise AI & Automation"),
        skill_line("Systems, Workflow & Governance"),
        skill_line("Analytics & Reporting"),
        skill_line("Product, PMO & Stakeholder Operations"),
        f"    \\textbf{{Tools:}} {latex_escape(', '.join(map(str, skills.get('Tools', []) or [])))}",
        r"    }}",
        r"\end{itemize}",
        r"\vspace{-10pt}",
        r"\section{Education}",
        r"  \resumeSubHeadingListStart",
        r"\resumeSubheading",
        r"      {M.S. Technology Management -- University of Illinois, Urbana Champaign}{\textit{Aug 2023 -- Aug 2024}}",
        r"      {}{}",
        r"      \vspace{-20pt}",
        r"    \resumeSubHeadingListEnd",
        "",
        r"\end{document}",
    ])
    return "\n".join(lines) + "\n"


def run_pipeline(args: argparse.Namespace) -> list[AgentResult]:
    base_output_dir = Path(args.output_dir)
    base_output_dir.mkdir(parents=True, exist_ok=True)

    jd_text = read_text(Path(args.jd))
    if not jd_text.strip():
        raise ValueError(f"Job description is empty: {args.jd}")

    jd_profile = analyze_jd(jd_text)
    run_name = slugify("_".join(part for part in [jd_profile.get("company_name", ""), jd_profile.get("role_title", "")] if part))
    output_dir = base_output_dir / run_name
    if output_dir.exists() and not args.no_clean:
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_text(output_dir / "input_job_description.txt", jd_text)
    write_text(output_dir / "01_jd_profile.json", json.dumps(jd_profile, indent=2, ensure_ascii=False))

    selected = select_evidence(jd_profile, Path(args.experiences))
    write_text(output_dir / "02_selected_evidence.json", json.dumps(selected, indent=2, ensure_ascii=False))

    results: list[AgentResult] = []
    writer = run_codex_json(
        "03_resume_writer",
        writer_prompt(jd_profile, selected),
        output_dir / "03_resume_content.json",
        output_dir,
        args.model,
    )
    results.append(writer)
    content = normalize_resume_content(json.loads(read_text(writer.output_path)), jd_profile)
    write_text(writer.output_path, json.dumps(content, indent=2, ensure_ascii=False))

    unsupported_tools = unsupported_jd_tools(jd_profile, selected)
    check = validate(content, unsupported_tools)
    write_text(output_dir / "05_rule_check.json", json.dumps(check, indent=2, ensure_ascii=False))
    for attempt in range(args.revision_attempts):
        if check["status"] == "pass":
            break
        revision = run_codex_json(
            f"03b_resume_revision_{attempt + 1}",
            revision_prompt(jd_profile, selected, content, check),
            output_dir / "03_resume_content.json",
            output_dir,
            args.model,
        )
        results.append(revision)
        content = normalize_resume_content(json.loads(read_text(revision.output_path)), jd_profile)
        write_text(revision.output_path, json.dumps(content, indent=2, ensure_ascii=False))
        check = validate(content, unsupported_tools)
        write_text(output_dir / "05_rule_check.json", json.dumps(check, indent=2, ensure_ascii=False))

    write_text(output_dir / "04_final_resume.tex", render_latex(content))
    args.resolved_output_dir = output_dir
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a tailored LaTeX resume from a JD and experience JSONs.")
    parser.add_argument("--jd", default="job_description.txt")
    parser.add_argument("--experiences", default="experiences")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default=None)
    parser.add_argument("--revision-attempts", type=int, default=2)
    parser.add_argument("--no-clean", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run_pipeline(args)
    resolved_dir = getattr(args, "resolved_output_dir", Path(args.output_dir))
    print("Resume pipeline complete:")
    for result in results:
        print(f"- {result.name}: {result.output_path}")
    print(f"- rule_check: {resolved_dir / '05_rule_check.json'}")
    print(f"- final_resume: {resolved_dir / '04_final_resume.tex'}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)




