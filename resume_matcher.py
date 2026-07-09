#!/usr/bin/env python3
"""
Resume experience matcher.

Usage:
  python resume_matcher.py --product
  python resume_matcher.py
  python resume_matcher.py --jd job_description.txt
  python resume_matcher.py --jd job_description.txt --use-llm --model gpt-4.1-mini
  python resume_matcher.py --jd job_description.txt --format codex --output codex_prompt.md
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.request
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "it",
    "of",
    "on",
    "or",
    "our",
    "that",
    "the",
    "their",
    "this",
    "to",
    "with",
    "you",
    "your",
    "will",
    "we",
    "about",
    "candidate",
    "company",
    "job",
    "learn",
    "looking",
    "more",
    "need",
    "role",
    "skills",
    "summary",
    "team",
    "teams",
}

SKILL_HINTS = [
    "SQL",
    "Python",
    "Tableau",
    "Power BI",
    "Excel",
    "Salesforce",
    "JIRA",
    "Azure DevOps",
    "SharePoint",
    "Agile",
    "Scrum",
    "SDLC",
    "ETL",
    "QA",
    "UAT",
    "CRM",
    "SaaS",
    "stakeholder management",
    "requirements gathering",
    "business analysis",
    "data analysis",
    "project management",
    "program management",
    "process improvement",
    "cross-functional",
    "customer success",
    "revenue operations",
    "product operations",
    "implementation",
    "digital transformation",
]


@dataclass(frozen=True)
class WeightedTerm:
    value: str
    weight: float


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(normalize_text(item) for item in value)
    if isinstance(value, dict):
        return " ".join(normalize_text(item) for item in value.values())
    return str(value)


def tokenize(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]*", text.lower())
    cleaned = [token.strip(".,;:!?()[]{}") for token in tokens]
    return [token for token in cleaned if token not in STOPWORDS and len(token) > 1]


def phrase_present(phrase: str, text: str) -> bool:
    return re.search(rf"\b{re.escape(phrase.lower())}\b", text.lower()) is not None


def extract_metrics(text: str) -> list[str]:
    patterns = [
        r"\$[\d,.]+ ?[kmbKMB]?",
        r"\b\d+(?:\.\d+)?%",
        r"\b\d+(?:\.\d+)? ?(?:x|X)\b",
        r"\b\d+[+]?\s?(?:projects|users|clients|teams|workflows|dashboards|reports|sprints|stakeholders|meals|leads|campaigns|sequences|opportunities)\b",
    ]
    metrics: list[str] = []
    for pattern in patterns:
        metrics.extend(re.findall(pattern, text, flags=re.IGNORECASE))
    filtered = []
    for metric in metrics:
        clean = metric.strip()
        if re.search(r"\b(year|years|salary|annually|annual)\b", clean, flags=re.IGNORECASE):
            continue
        filtered.append(clean)
    return sorted(set(filtered))


def top_keywords(text: str, limit: int = 35) -> list[str]:
    words = tokenize(text)
    counts = Counter(words)
    return [word for word, _ in counts.most_common(limit)]


def extract_jd_profile_heuristic(jd_text: str) -> dict[str, Any]:
    jd_lower = jd_text.lower()
    hinted_skills = [skill for skill in SKILL_HINTS if phrase_present(skill, jd_lower)]
    role_title = extract_role_title(jd_text)

    competencies = []
    competency_patterns = {
        "Business Analysis": ["requirements", "business analysis", "user stories", "functional"],
        "Data Analysis": ["data", "analytics", "insights", "dashboard", "sql", "tableau"],
        "Project / Program Execution": ["project", "program", "timeline", "roadmap", "delivery"],
        "Stakeholder Management": ["stakeholder", "cross-functional", "leadership", "client"],
        "Process Improvement": ["process", "workflow", "operational efficiency", "standardize"],
        "Product Operations": ["product", "roadmap", "launch", "backlog", "release"],
        "Implementation / Systems": ["implementation", "systems", "integration", "uat", "qa"],
        "Revenue / Customer Value": ["revenue", "retention", "customer", "client value", "growth"],
    }
    for competency, needles in competency_patterns.items():
        if any(needle in jd_lower for needle in needles):
            competencies.append(competency)

    return {
        "role_title": role_title,
        "core_competencies": competencies[:10],
        "best_evidence": infer_best_evidence(jd_lower),
        "keywords": merge_unique(hinted_skills + top_keywords(jd_text)),
        "key_metrics": infer_key_metrics(jd_lower) + extract_jd_metrics(jd_text),
        "role_family": infer_role_family(jd_lower),
        "seniority": infer_seniority(jd_lower),
        "must_show": infer_must_show(jd_lower),
        "resume_strategy": infer_resume_strategy(jd_lower),
        "raw_text": jd_text,
        "source": "heuristic",
    }


def extract_role_title(jd_text: str) -> str:
    role_match = re.search(
        r"(?:title|role|position)\s*[:\-]\s*(.+)", jd_text, flags=re.IGNORECASE
    )
    if role_match:
        return role_match.group(1).strip()

    looking_match = re.search(
        r"looking for an? ([A-Z][A-Za-z0-9 /&,+.-]{3,80}?) to ",
        jd_text,
        flags=re.IGNORECASE,
    )
    if looking_match:
        return looking_match.group(1).strip()

    for line in jd_text.splitlines()[:12]:
        clean = line.strip(" \t-#:")
        if not clean or len(clean) > 90:
            continue
        if any(term in clean.lower() for term in ["http", ".com", "learn more", "about us", "about the job"]):
            continue
        if re.search(
            r"\b(analyst|associate|manager|coordinator|specialist|consultant|operations|product|program|business)\b",
            clean,
            flags=re.IGNORECASE,
        ):
            return clean
    return ""


def infer_role_family(jd_lower: str) -> str:
    families = [
        ("Product Operations", ["product operations", "roadmap", "launch", "backlog"]),
        ("Business Systems / Business Analyst", ["business systems", "requirements", "user stories", "uat"]),
        ("Program / Project Operations", ["program", "project", "timeline", "milestone", "jira"]),
        ("Revenue / GTM Operations", ["revenue", "sales operations", "gtm", "pipeline", "forecast"]),
        ("Customer Success / Value", ["customer success", "retention", "churn", "customer value"]),
        ("Data / BI Analyst", ["sql", "tableau", "power bi", "dashboard", "analytics"]),
        ("Process / Digital Transformation", ["process improvement", "workflow", "transformation", "automation"]),
    ]
    scores = [
        (sum(1 for needle in needles if needle in jd_lower), family)
        for family, needles in families
    ]
    best_score, best_family = max(scores)
    return best_family if best_score else "General Operations / Analyst"


def infer_seniority(jd_lower: str) -> str:
    if any(term in jd_lower for term in ["senior", "sr.", "lead", "principal"]):
        return "Senior / Lead"
    if any(term in jd_lower for term in ["intern", "entry-level", "entry level", "junior"]):
        return "Entry / Junior"
    if any(term in jd_lower for term in ["manager", "own", "ownership", "drive"]):
        return "Mid-level with ownership"
    return "Analyst / Associate"


def infer_must_show(jd_lower: str) -> list[str]:
    signals = []
    checks = [
        ("Requirements and stakeholder translation", ["requirements", "stakeholder", "business analysis"]),
        ("Data-backed recommendations", ["sql", "analytics", "data", "insights", "dashboard"]),
        ("Cross-functional execution", ["cross-functional", "engineering", "product", "sales", "marketing"]),
        ("Process or workflow improvement", ["process", "workflow", "efficiency", "standardize"]),
        ("Agile delivery or roadmap tracking", ["agile", "scrum", "jira", "roadmap", "backlog", "sprint"]),
        ("Implementation, UAT, or release readiness", ["implementation", "uat", "release", "launch", "go-live"]),
        ("Customer, revenue, or retention impact", ["customer", "retention", "revenue", "growth", "churn"]),
        ("Executive-ready communication", ["executive", "leadership", "senior management", "presentation"]),
    ]
    for label, needles in checks:
        if any(needle in jd_lower for needle in needles):
            signals.append(label)
    return signals


def infer_resume_strategy(jd_lower: str) -> list[str]:
    strategy = []
    if any(term in jd_lower for term in ["requirements", "stakeholder", "business analysis"]):
        strategy.append("Lead with BA-style bullets that translate ambiguous needs into clear requirements and execution plans.")
    if any(term in jd_lower for term in ["sql", "dashboard", "analytics", "data"]):
        strategy.append("Show data analysis as decision support, not just reporting.")
    if any(term in jd_lower for term in ["process", "workflow", "efficiency"]):
        strategy.append("Frame operational work around measurable workflow improvement.")
    if any(term in jd_lower for term in ["product", "roadmap", "launch", "backlog"]):
        strategy.append("Use product-operations language: roadmap, delivery cadence, launches, adoption, and feedback loops.")
    if any(term in jd_lower for term in ["customer", "retention", "revenue"]):
        strategy.append("Tie work to customer value, retention, revenue protection, or business outcomes.")
    return strategy or ["Emphasize analyst ownership, structured execution, stakeholder alignment, and measurable business impact."]


def infer_best_evidence(jd_lower: str) -> list[str]:
    evidence = []
    if any(term in jd_lower for term in ["requirements", "user story", "functional spec"]):
        evidence.append("requirements translated into functional specifications")
    if any(term in jd_lower for term in ["sql", "dashboard", "analytics", "reporting"]):
        evidence.append("analysis, reporting, dashboards, or decision-support artifacts")
    if any(term in jd_lower for term in ["stakeholder", "cross-functional", "leadership"]):
        evidence.append("cross-functional stakeholder coordination")
    if any(term in jd_lower for term in ["process", "workflow", "efficiency"]):
        evidence.append("workflow/process improvement with measurable efficiency gains")
    if any(term in jd_lower for term in ["launch", "implementation", "release", "uat"]):
        evidence.append("implementation, testing, release, or launch readiness work")
    if any(term in jd_lower for term in ["revenue", "retention", "customer", "growth"]):
        evidence.append("customer, revenue, retention, or growth impact")
    return evidence[:8]


def infer_key_metrics(jd_lower: str) -> list[str]:
    metrics = []
    if "retention" in jd_lower:
        metrics.append("retention improvement")
    if "revenue" in jd_lower:
        metrics.append("revenue impact")
    if "efficiency" in jd_lower or "process" in jd_lower:
        metrics.append("efficiency improvement")
    if "defect" in jd_lower or "quality" in jd_lower:
        metrics.append("defect reduction / quality improvement")
    if "dashboard" in jd_lower or "report" in jd_lower:
        metrics.append("number of reports or dashboards delivered")
    if "stakeholder" in jd_lower or "cross-functional" in jd_lower:
        metrics.append("number of stakeholders or teams supported")
    return metrics


def extract_jd_metrics(jd_text: str) -> list[str]:
    metrics = []
    for metric in extract_metrics(jd_text):
        index = jd_text.lower().find(metric.lower())
        window = jd_text[max(0, index - 80) : index + len(metric) + 80].lower()
        if any(term in window for term in ["salary", "benefits", "compensation", "range of"]):
            continue
        if re.search(r"\$\d", metric):
            continue
        metrics.append(metric)
    return metrics


def merge_unique(values: list[str]) -> list[str]:
    seen = set()
    merged = []
    for value in values:
        clean = value.strip()
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            merged.append(clean)
    return merged


def load_experiences(experience_dir: Path) -> list[dict[str, Any]]:
    files = sorted(experience_dir.glob("*.json"))
    if not files:
        raise FileNotFoundError(f"No JSON files found in {experience_dir}")

    experiences = []
    for file_path in files:
        with file_path.open("r", encoding="utf-8-sig") as handle:
            data = json.load(handle)
        data["_file"] = str(file_path)
        experiences.append(data)
    return experiences


def build_jd_terms(jd_profile: dict[str, Any]) -> list[WeightedTerm]:
    fields = [
        ("role_title", 4.0),
        ("core_competencies", 5.0),
        ("best_evidence", 4.0),
        ("keywords", 3.0),
        ("key_metrics", 3.0),
    ]
    terms: list[WeightedTerm] = []
    for field, weight in fields:
        value = jd_profile.get(field, "")
        if isinstance(value, str):
            values = [value]
        else:
            values = list(value or [])
        for item in values:
            item = str(item).strip()
            if item:
                terms.append(WeightedTerm(item, weight))
                for token in tokenize(item):
                    terms.append(WeightedTerm(token, max(1.0, weight * 0.5)))
    return terms


def score_point(point: dict[str, Any], jd_profile: dict[str, Any]) -> dict[str, Any]:
    tags = point.get("tags", {})
    searchable = normalize_text(
        [
            point.get("point_title"),
            point.get("base_resume_point"),
            tags.get("core_competency"),
            tags.get("functional_skill"),
            tags.get("business_outcome"),
            tags.get("evidence_proof"),
            tags.get("metric_placeholder"),
            tags.get("best_fit_roles"),
            tags.get("secondary_fit_roles"),
            tags.get("adaptation_direction"),
        ]
    ).lower()

    matched_terms: list[str] = []
    score = 0.0
    for term in build_jd_terms(jd_profile):
        term_value = term.value.lower()
        if phrase_present(term_value, searchable):
            score += term.weight
            matched_terms.append(term.value)

    jd_tokens = set(tokenize(normalize_text(jd_profile)))
    point_tokens = set(tokenize(searchable))
    overlap = jd_tokens.intersection(point_tokens)
    score += len(overlap) * 0.35

    if extract_metrics(normalize_text(tags.get("metric_placeholder"))):
        score += 2.0
    if tags.get("evidence_proof"):
        score += 2.0

    return {
        "score": round(score, 2),
        "matched_terms": merge_unique(matched_terms)[:20],
        "token_overlap": sorted(overlap)[:30],
    }


def choose_relevant_adaptation(point: dict[str, Any], jd_profile: dict[str, Any]) -> list[str]:
    directions = point.get("tags", {}).get("adaptation_direction", [])
    if not directions:
        return []
    jd_text = normalize_text(jd_profile).lower()
    scored = []
    for direction in directions:
        overlap = set(tokenize(direction)).intersection(set(tokenize(jd_text)))
        scored.append((len(overlap), direction))
    return [direction for _, direction in sorted(scored, reverse=True)[:3]]


def adaptation_angle(direction: str) -> str:
    match = re.search(
        r"frame(?: carefully)? as (.+?)(?:\.|$)", direction, flags=re.IGNORECASE
    )
    if match:
        return match.group(1).strip()
    cleaned = re.sub(r"^For [^,]+,\s*", "", direction.strip(), flags=re.IGNORECASE)
    return cleaned.rstrip(".")


def choose_metric(metrics: list[str]) -> str:
    for metric in metrics:
        if re.search(r"\d|%|\$", metric):
            return metric
    return ""


def adapt_point_heuristic(point: dict[str, Any], jd_profile: dict[str, Any]) -> str:
    base = point.get("base_resume_point", "").strip()
    evidence = point.get("tags", {}).get("evidence_proof", [])
    metrics = point.get("tags", {}).get("metric_placeholder", [])
    directions = choose_relevant_adaptation(point, jd_profile)

    proof = evidence[0] if evidence else ""
    metric = choose_metric(metrics)
    angle = adaptation_angle(directions[0]) if directions else ""

    adapted = base.rstrip(".")
    if angle and angle.lower() not in adapted.lower():
        adapted = f"{adapted}, emphasizing {angle}"
    if metric and metric.lower() not in adapted.lower():
        adapted = f"{adapted}, with impact measured through {metric}"
    elif proof and proof.lower() not in adapted.lower():
        adapted = f"{adapted}, backed by {proof[0].lower() + proof[1:] if proof else proof}"

    adapted = re.sub(r"\s+", " ", adapted).strip().rstrip(",")
    if not adapted.endswith("."):
        adapted = f"{adapted}."
    return adapted


def call_openai_json(prompt: str, model: str) -> dict[str, Any]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    payload = {
        "model": model,
        "input": prompt,
        "text": {"format": {"type": "json_object"}},
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"OpenAI API error {exc.code}: {body}") from exc

    text_blocks = []
    for item in data.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text":
                text_blocks.append(content.get("text", ""))
    if not text_blocks:
        raise RuntimeError("OpenAI response did not include output_text")
    return json.loads("\n".join(text_blocks))


def extract_jd_profile_llm(jd_text: str, model: str) -> dict[str, Any]:
    prompt = f"""
Extract a resume-targeting profile from this job description.

Return JSON with exactly these keys:
- role_title: string
- core_competencies: array of concise competencies
- best_evidence: array of evidence types the resume should prove
- keywords: array of ATS and recruiter keywords
- key_metrics: array of metrics or impact signals worth showing

Job description:
{jd_text}
"""
    profile = call_openai_json(prompt, model)
    profile["raw_text"] = jd_text
    profile["source"] = f"llm:{model}"
    return profile


def adapt_point_llm(
    point: dict[str, Any], jd_profile: dict[str, Any], model: str
) -> str:
    prompt = f"""
Rewrite this base resume bullet to align with the target job description profile.

Rules:
- Keep the claim truthful to the evidence.
- Use strong resume language.
- Prefer measurable impact when a metric placeholder contains an actual number.
- Do not invent employers, tools, numbers, or outcomes.
- Return JSON: {{"resume_point": "..."}}

JD profile:
{json.dumps(jd_profile, indent=2)}

Experience point:
{json.dumps(point, indent=2)}
"""
    return call_openai_json(prompt, model)["resume_point"]


def match_experiences(
    experiences: list[dict[str, Any]],
    jd_profile: dict[str, Any],
    top_n: int,
    use_llm: bool,
    model: str,
) -> dict[str, Any]:
    output = {
        "jd_profile": jd_profile,
        "matches": [],
    }
    for experience in experiences:
        scored_points = []
        for point in experience.get("points", []):
            score_data = score_point(point, jd_profile)
            scored_points.append((score_data["score"], point, score_data))

        selected = sorted(scored_points, key=lambda item: item[0], reverse=True)[:top_n]
        match_items = []
        for rank, (_, point, score_data) in enumerate(selected, start=1):
            if use_llm:
                adapted = adapt_point_llm(point, jd_profile, model)
            else:
                adapted = adapt_point_heuristic(point, jd_profile)
            match_items.append(
                {
                    "rank": rank,
                    "id": point.get("id"),
                    "point_title": point.get("point_title"),
                    "score": score_data["score"],
                    "matched_terms": score_data["matched_terms"],
                    "token_overlap": score_data["token_overlap"],
                    "base_resume_point": point.get("base_resume_point"),
                    "adapted_resume_point": adapted,
                    "evidence_proof": point.get("tags", {}).get("evidence_proof", []),
                    "metric_placeholder": point.get("tags", {}).get(
                        "metric_placeholder", []
                    ),
                    "adaptation_direction": choose_relevant_adaptation(
                        point, jd_profile
                    ),
                }
            )

        output["matches"].append(
            {
                "experience_source": experience.get("experience_source"),
                "experience_file": experience.get("_file"),
                "top_points": match_items,
            }
        )
    return output


def render_markdown(result: dict[str, Any]) -> str:
    profile = result["jd_profile"]
    lines = [
        "# Resume Match Report",
        "",
        f"JD extraction source: `{profile.get('source', 'unknown')}`",
        f"Role title: {profile.get('role_title') or 'Not detected'}",
        "",
        "## Core Competencies",
        "",
    ]
    lines.extend(f"- {item}" for item in profile.get("core_competencies", []))
    lines.extend(["", "## Keywords", ""])
    lines.append(", ".join(profile.get("keywords", [])[:50]) or "None detected")
    lines.extend(["", "## Key Metrics", ""])
    lines.extend(f"- {item}" for item in profile.get("key_metrics", []))

    for match in result["matches"]:
        lines.extend(["", f"## {match['experience_source']}", ""])
        for item in match["top_points"]:
            lines.append(f"### {item['rank']}. {item['point_title']} ({item['score']})")
            lines.append("")
            lines.append(f"ID: `{item['id']}`")
            lines.append("")
            lines.append(f"Adapted: {item['adapted_resume_point']}")
            lines.append("")
            lines.append(f"Base: {item['base_resume_point']}")
            lines.append("")
            if item["matched_terms"]:
                lines.append("Matched terms: " + ", ".join(item["matched_terms"]))
                lines.append("")
            if item["evidence_proof"]:
                lines.append("Evidence:")
                lines.extend(f"- {evidence}" for evidence in item["evidence_proof"])
                lines.append("")
            if item["metric_placeholder"]:
                lines.append("Metric angles:")
                lines.extend(f"- {metric}" for metric in item["metric_placeholder"])
                lines.append("")
    return "\n".join(lines).strip() + "\n"


def all_ranked_points(result: dict[str, Any], limit: int = 15) -> list[dict[str, Any]]:
    ranked = []
    for match in result["matches"]:
        for item in match["top_points"]:
            ranked.append(
                {
                    **item,
                    "experience_source": match["experience_source"],
                    "experience_file": match["experience_file"],
                }
            )
    return sorted(ranked, key=lambda item: item["score"], reverse=True)[:limit]


def render_jd_intelligence(result: dict[str, Any]) -> str:
    profile = result["jd_profile"]
    lines = [
        "# JD Intelligence Brief",
        "",
        f"Role title: {profile.get('role_title') or 'Not detected'}",
        f"Role family: {profile.get('role_family', 'Not detected')}",
        f"Seniority read: {profile.get('seniority', 'Not detected')}",
        f"Extraction source: {profile.get('source', 'heuristic')}",
        "",
        "## Core Competencies",
        "",
    ]
    lines.extend(f"- {item}" for item in profile.get("core_competencies", []))
    lines.extend(["", "## Must Show In Resume", ""])
    lines.extend(f"- {item}" for item in profile.get("must_show", []))
    lines.extend(["", "## Best Evidence To Use", ""])
    lines.extend(f"- {item}" for item in profile.get("best_evidence", []))
    lines.extend(["", "## Metric Angles", ""])
    lines.extend(f"- {item}" for item in profile.get("key_metrics", []))
    lines.extend(["", "## Resume Strategy", ""])
    lines.extend(f"- {item}" for item in profile.get("resume_strategy", []))
    lines.extend(["", "## ATS / Recruiter Keywords", ""])
    lines.append(", ".join(profile.get("keywords", [])[:70]) or "None detected")
    return "\n".join(lines).strip() + "\n"


def render_final_workspace(result: dict[str, Any]) -> str:
    profile = result["jd_profile"]
    best_points = all_ranked_points(result, limit=18)
    lines = [
        "# Final Resume Bullets Workspace",
        "",
        "This file is the working area for final tailored bullets.",
        "Use the evidence bank below to create the final version.",
        "",
        "## Target",
        "",
        f"- Role: {profile.get('role_title') or 'Unknown'}",
        f"- Role family: {profile.get('role_family', 'Unknown')}",
        f"- Seniority: {profile.get('seniority', 'Unknown')}",
        "",
        "## Final Bullets",
        "",
        "Replace these placeholders with final Codex-written bullets.",
        "",
    ]
    for match in result["matches"]:
        lines.extend([f"### {match['experience_source']}", ""])
        for item in match["top_points"][:3]:
            lines.append(f"- TODO: Rewrite `{item['id']}` for the target role.")
        lines.append("")

    lines.extend(["## Best Evidence Bank", ""])
    for item in best_points:
        lines.extend(
            [
                f"### {item['experience_source']} - {item['id']} ({item['score']})",
                "",
                f"Base: {item['base_resume_point']}",
                "",
                f"Suggested draft: {item['adapted_resume_point']}",
                "",
            ]
        )
        if item["evidence_proof"]:
            lines.append("Evidence:")
            lines.extend(f"- {evidence}" for evidence in item["evidence_proof"])
            lines.append("")
        if item["metric_placeholder"]:
            lines.append("Metrics:")
            lines.extend(f"- {metric}" for metric in item["metric_placeholder"])
            lines.append("")
    return "\n".join(lines).strip() + "\n"


def render_modified_points_only(result: dict[str, Any]) -> str:
    lines = ["# Modified Resume Points", ""]
    for match in result["matches"]:
        lines.extend([f"## {match['experience_source']}", ""])
        for item in match["top_points"]:
            lines.append(f"- {item['adapted_resume_point']}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in text)


def plain_word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9$]+", text))


def fit_word_count(text: str, target: int) -> str:
    words = text.strip().rstrip(".").split()
    while len(words) > target and words[-1].strip(",;:").lower() in {
        "and",
        "or",
        "with",
        "across",
        "for",
        "to",
        "into",
        "by",
    }:
        words.pop()
    if len(words) > target:
        words = words[:target]
    pads = [
        "across teams",
        "with clean handoffs",
        "for leaders",
        "across workflows",
        "with measurable impact",
        "for execution",
    ]
    pad_index = 0
    while len(words) < target and pad_index < len(pads):
        candidate = pads[pad_index].split()
        if len(words) + len(candidate) <= target:
            words.extend(candidate)
        pad_index += 1
    while len(words) < target:
        words.append("impact")
    sentence = " ".join(words).strip(" ,;:")
    return f"{sentence}."


def exact_phrase(text: str, target: int) -> str:
    words = text.strip().rstrip(".").split()
    if len(words) == target:
        return f"{' '.join(words)}."
    return text.strip() if text.strip().endswith(".") else f"{text.strip()}."


def clean_resume_sentence(text: str) -> str:
    text = re.sub(r"\bemphasizing For [^,]+,\s*", "emphasizing ", text)
    text = re.sub(r"\bMetric angle:\s*", "", text)
    text = re.sub(r"\bEvidence:\s*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text if text.endswith(".") else f"{text}."


def jd_language(profile: dict[str, Any]) -> dict[str, bool]:
    jd_text = normalize_text(profile).lower()
    return {
        "revops": any(term in jd_text for term in ["revenue", "pipeline", "revops"]),
        "crm": any(term in jd_text for term in ["crm", "hubspot", "salesforce"]),
        "data_flow": any(term in jd_text for term in ["data flow", "handoff", "integrations", "leads flow"]),
        "reporting": any(term in jd_text for term in ["reporting", "qbr", "board", "metrics"]),
        "lifecycle": any(term in jd_text for term in ["lifecycle", "lead routing", "lead scoring", "campaign"]),
        "sales_marketing": any(term in jd_text for term in ["sales", "marketing", "growth leadership"]),
    }


def jd_short_tail(profile: dict[str, Any]) -> str:
    family = profile.get("role_family", "").lower()
    jd_text = normalize_text(profile).lower()
    if "revenue" in family or "pipeline" in jd_text:
        return "to improve pipeline reporting, data hygiene, stakeholder visibility, and clean handoffs consistently"
    if "customer" in family:
        return "to improve customer value, retention visibility, service quality, and decision support consistently"
    if "business systems" in family or "requirements" in jd_text:
        return "to improve requirements clarity, system alignment, stakeholder handoffs, and execution visibility consistently"
    if "product" in family:
        return "to improve roadmap execution, launch readiness, stakeholder alignment, and adoption visibility consistently"
    if "data" in family or "dashboard" in jd_text:
        return "to improve insight reporting, KPI visibility, stakeholder decisions, and analytical quality consistently"
    return "to improve workflow clarity, documentation quality, operating cadence, and cross-functional execution consistently"


def jd_long_tail(profile: dict[str, Any]) -> str:
    family = profile.get("role_family", "").lower()
    jd_text = normalize_text(profile).lower()
    if "revenue" in family or "pipeline" in jd_text:
        return "improving pipeline reporting, data hygiene, source-of-truth visibility, stakeholder alignment, clean handoffs, and repeatable execution across sales, marketing, and operations."
    if "customer" in family:
        return "improving customer insight, retention visibility, service quality, stakeholder alignment, repeatable decisions, and value delivery across client-facing teams."
    if "business systems" in family or "requirements" in jd_text:
        return "improving requirements clarity, process documentation, UAT readiness, stakeholder alignment, clean handoffs, and repeatable execution across business and technical teams."
    if "product" in family:
        return "improving roadmap visibility, delivery cadence, launch readiness, stakeholder alignment, feedback loops, and adoption across product and cross-functional teams."
    if "data" in family or "dashboard" in jd_text:
        return "improving KPI visibility, reporting quality, analytical decision-making, stakeholder alignment, repeatable insights, and data-backed execution across business teams."
    return "improving workflow visibility, documentation quality, operating cadence, stakeholder alignment, clean handoffs, and cross-functional execution across business teams."


def point_action_object(item: dict[str, Any]) -> str:
    title = f"{item.get('point_title', '')} {item.get('base_resume_point', '')}".lower()
    source = item.get("experience_source", "").lower()
    if "salesforce" in source and ("governance" in title or "approval" in title):
        return "Owned Salesforce governance"
    if "salesforce" in source and ("article" in title or "knowledge" in title):
        return "Consolidated Salesforce knowledge"
    if "salesforce" in source and ("audit" in title or "customer service" in title):
        return "Audited service workflows"
    if "operating model" in title:
        return "Built operating cadence"
    if "sql" in title or "data analysis" in title:
        return "Analyzed SQL data"
    if "report" in title or "visual" in title or "tableau" in title:
        return "Built insight reporting"
    if "requirement" in title or "specification" in title:
        return "Translated stakeholder needs"
    if "sharepoint" in title or "intranet" in title:
        return "Centralized workflow documentation"
    if "roadmap" in title or "execution" in title:
        return "Owned roadmap execution"
    if "financial" in title or "revenue" in title or "profitability" in title:
        return "Analyzed revenue impact"
    if "defect" in title:
        return "Managed defect prioritization"
    if "etl" in title or "migration" in title:
        return "Validated migration data"
    if "test" in title or "qa" in title:
        return "Documented release validation"
    if "ai" in title or "0-to-1" in title:
        return "Launched analytics product"
    return "Improved operating workflows"


def point_context(item: dict[str, Any]) -> str:
    title = f"{item.get('point_title', '')} {item.get('base_resume_point', '')}".lower()
    metrics = item.get("metric_placeholder", [])
    metric = choose_metric(metrics)
    if metric:
        return f"using evidence including {metric}"
    if "salesforce" in item.get("experience_source", "").lower():
        return "using Salesforce operating evidence"
    if "sql" in title:
        return "using SQL analysis and customer data"
    if "tableau" in title or "visual" in title:
        return "using dashboards and visual reporting"
    if "sharepoint" in title:
        return "using centralized SharePoint workflows"
    if "requirements" in title:
        return "using stakeholder requirements and specifications"
    if "etl" in title:
        return "using ETL validation and reconciliation"
    return "using documented execution evidence"


def exact_resume_bullet(item: dict[str, Any], profile: dict[str, Any], target_words: int) -> str:
    action = point_action_object(item)
    if target_words <= 15:
        text = f"{action} {jd_short_tail(profile)}."
    else:
        text = f"{action} using documented evidence, {jd_long_tail(profile)}"
    return exact_phrase(text, target_words)


def aligned_bullet(item: dict[str, Any], profile: dict[str, Any], source: str, target_words: int) -> str:
    item = {**item, "experience_source": source}
    return exact_resume_bullet(item, profile, target_words)


def find_match(result: dict[str, Any], source_contains: str) -> dict[str, Any] | None:
    for match in result["matches"]:
        if source_contains.lower() in match["experience_source"].lower():
            return match
    return None


def find_marketmaker_ba(result: dict[str, Any]) -> dict[str, Any] | None:
    for match in result["matches"]:
        source = match["experience_source"].lower()
        if source == "marketmaker cre":
            return match
    return find_match(result, "MarketMaker CRE")


def ordered_points(match: dict[str, Any] | None, count: int, profile: dict[str, Any]) -> list[str]:
    if not match:
        return []
    targets = [15, 28] * ((count + 1) // 2)
    source = match["experience_source"]
    return [
        aligned_bullet(item, profile, source, targets[index])
        for index, item in enumerate(match["top_points"][:count])
    ]


def render_latex_resume(result: dict[str, Any]) -> str:
    profile = result["jd_profile"]
    role_title = profile.get("role_title") or profile.get("role_family") or "Operations Analyst"
    must_show = profile.get("must_show", [])
    keywords = profile.get("keywords", [])
    focus_one = must_show[0].lower() if must_show else "systems and process ownership"
    focus_two = must_show[1].lower() if len(must_show) > 1 else "stakeholder visibility"
    keyword_text = ", ".join(keywords[:4])
    summary = (
        f"{role_title} candidate with evidence in {focus_one}, {focus_two}, reporting, and repeatable workflows. "
        f"Experienced translating {keyword_text} priorities into structured execution, documentation, data quality, stakeholder alignment, and measurable business impact."
    )
    if plain_word_count(summary) > 45:
        summary = (
            f"{role_title} candidate with experience in {focus_one}, reporting, repeatable workflows, data quality, "
            "stakeholder alignment, documentation, and measurable business impact across systems, operations, analytics, and transformation work."
        )

    salesforce = ordered_points(find_match(result, "Salesforce"), 5, profile)
    marketmaker_pm = ordered_points(find_match(result, "Promotion"), 3, profile)
    marketmaker_ba = ordered_points(find_marketmaker_ba(result), 3, profile)
    vista = ordered_points(find_match(result, "Vista"), 4, profile)
    ltim = ordered_points(find_match(result, "LTIMindtree"), 4, profile)

    def items(points: list[str]) -> str:
        return "\n".join(f"\\resumeItem{{{latex_escape(point)}}}" for point in points)

    return f"""\\documentclass[letterpaper,10pt]{{article}}
\\usepackage{{latexsym}}
\\usepackage[empty]{{fullpage}}
\\usepackage{{titlesec}}
\\usepackage{{marvosym}}
\\usepackage[usenames,dvipsnames]{{color}}
\\usepackage{{verbatim}}
\\usepackage{{enumitem}}
\\usepackage[hidelinks]{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage[english]{{babel}}
\\usepackage{{tabularx}}
\\usepackage{{fontawesome5}}
\\usepackage{{multicol}}
\\setlength{{\\multicolsep}}{{-3.0pt}}
\\setlength{{\\columnsep}}{{-1pt}}
\\input{{glyphtounicode}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\renewcommand{{\\headrulewidth}}{{0pt}}
\\renewcommand{{\\footrulewidth}}{{0pt}}
\\addtolength{{\\oddsidemargin}}{{-0.6in}}
\\addtolength{{\\evensidemargin}}{{-0.5in}}
\\addtolength{{\\textwidth}}{{1.19in}}
\\addtolength{{\\topmargin}}{{-.7in}}
\\addtolength{{\\textheight}}{{1.4in}}
\\raggedbottom
\\raggedright
\\setlength{{\\tabcolsep}}{{0in}}
\\pdfgentounicode=1

\\newcommand{{\\resumeItem}}[1]{{\\item \\small{{#1}}}}
\\newcommand{{\\resumeSubheading}}[4]{{
  \\vspace{{1pt}}\\item
    \\begin{{tabular*}}{{1.0\\textwidth}}[t]{{l@{{\\extracolsep{{\\fill}}}}r}}
      \\textbf{{#1}} & \\textbf{{\\small #2}} \\\\
      \\textit{{\\small #3}} & \\textit{{\\small #4}} \\\\
    \\end{{tabular*}}\\vspace{{-6pt}}
}}
\\newcommand{{\\resumeSubHeadingListStart}}{{\\begin{{itemize}}[leftmargin=0.0in, label={{}}]}}
\\newcommand{{\\resumeSubHeadingListEnd}}{{\\end{{itemize}}}}
\\newcommand{{\\resumeItemListStart}}{{\\begin{{itemize}}[leftmargin=0.15in, itemsep=1pt, topsep=3pt]}}
\\newcommand{{\\resumeItemListEnd}}{{\\end{{itemize}}\\vspace{{-2pt}}}}
\\renewcommand\\labelitemi{{\\textbullet}}
\\renewcommand\\labelitemii{{\\textbullet}}
\\titleformat{{\\section}}{{\\vspace{{-4pt}}\\scshape\\raggedright\\large\\bfseries\\color{{MidnightBlue}}}}{{}}{{0em}}{{}}[\\color{{MidnightBlue}}\\titlerule \\vspace{{-5pt}}]

\\begin{{document}}

\\begin{{center}}
    {{\\Huge \\scshape Aishwarya Chourasia}} \\\\ \\vspace{{1pt}}
    \\small \\raisebox{{-0.1\\height}}\\faPhone\\ +1 217-607-7336 ~
    \\href{{mailto:aishwarya7uiuc@gmail.com}}{{\\raisebox{{-0.2\\height}}\\faEnvelope\\ aishwarya7uiuc@gmail.com}} ~
    \\href{{https://linkedin.com/in/aishwarya-chourasia-65b381151/}}{{\\raisebox{{-0.2\\height}}\\faLinkedin\\ LinkedIn}} ~
    \\href{{https://aishwarya2510.github.io/portfolio_new/}}{{\\raisebox{{-0.2\\height}}\\faBriefcase\\ Portfolio}}
\\end{{center}}

\\section{{Summary}}
 \\begin{{itemize}}[leftmargin=0.0in, label={{}}]
   \\item \\small{{{latex_escape(summary)}}}
 \\end{{itemize}}
\\vspace{{-10pt}}

\\section{{Experience}}
  \\resumeSubHeadingListStart

\\resumeSubheading
{{Salesforce}}{{USA}}
{{RevOps, Finance Operations \\& P2C Transformation}}{{Apr 2025 -- Mar 2026}}
\\resumeItemListStart
{items(salesforce)}
\\resumeItemListEnd

\\vspace{{-2pt}}

\\resumeSubheading
{{Market Maker CRE}}{{USA}}
{{Project Manager, Product Operations \\& Strategy}}{{Jan 2025 -- Apr 2025}}
\\resumeItemListStart
{items(marketmaker_pm)}
\\resumeItemListEnd

\\vspace{{-17pt}}

\\resumeSubheading
{{}}{{}}
{{Business Operations \\& Systems Analyst}}{{Aug 2024 -- Dec 2024}}
\\resumeItemListStart
{items(marketmaker_ba)}
\\resumeItemListEnd

\\vspace{{-2pt}}

\\resumeSubheading
{{Vista Research Services}}{{USA}}
{{AI Product, Marketing Analytics \\& Business Transformation Analyst}}{{May 2024 -- Apr 2025}}
\\resumeItemListStart
{items(vista)}
\\resumeItemListEnd

\\vspace{{-2pt}}

\\resumeSubheading
{{LTIMindtree}}{{India}}
{{Business Systems, Quality Operations \\& Cloud Transformation Analyst}}{{Aug 2021 -- Aug 2023}}
\\resumeItemListStart
{items(ltim)}
\\resumeItemListEnd

\\resumeSubHeadingListEnd
\\vspace{{-10pt}}

\\section{{Projects}}
  \\resumeSubHeadingListStart
\\resumeSubheading
{{Agent Maestro,\\textnormal{{\\textit{{ AI-Native Decision Intelligence Platform for Operations}}}}}}{{}}{{}}{{}}
\\vspace{{-17pt}}
\\resumeItemListStart
\\resumeItem{{Built AI decision layer across intake, classification, risk scoring, ownership, and approval routing.}}
\\resumeItem{{Modeled enterprise refund escalation, converting multi-team ambiguity into governed, risk-scored, owner-aligned execution flow.}}
\\resumeItemListEnd
\\vspace{{-3pt}}
\\resumeSubheading
{{Insight-to-Execution Operating Model,\\textnormal{{\\textit{{ Knowledge Operations, MCP Connectors \\& Multi-Agent Workflow Strategy}}}}}}{{}}{{}}{{}}
\\vspace{{-17pt}}
\\resumeItemListStart
\\resumeItem{{Designed operating model linking AI tools, knowledge operations, connectors, orchestration, governance, and ROI.}}
\\resumeItem{{Defined value metrics across cycle time, cost, adoption, governance exceptions, productivity, quality, and profitability.}}
\\resumeItemListEnd
\\resumeSubHeadingListEnd

\\vspace{{-10pt}}
\\section{{Skills}}
\\begin{{itemize}}[leftmargin=0.0in, label={{}}]
    \\small{{\\item{{
    \\textbf{{Revenue \\& Marketing Operations:}} Revenue Operations, Marketing Operations, Sales Enablement, Funnel KPIs, Lead Routing, Lifecycle Programs, Campaign Reporting, QBR Support \\\\
    \\textbf{{CRM, Systems \\& Process:}} Salesforce CRM, HubSpot Concepts, Data Hygiene, Workflow Automation, Source-of-Truth Reporting, UAT, SOPs, Runbooks, System Change Tickets \\\\
    \\textbf{{Analytics \\& Reporting:}} SQL, Excel, Tableau, Power BI, KPI Frameworks, Attribution, Pipeline Analysis, Executive Reporting, PowerPoint Narratives \\\\
    \\textbf{{Product \\& Business Operations:}} Roadmap Execution, Requirements Gathering, Stakeholder Management, Cross-Functional Delivery, Process Improvement, Documentation Governance \\\\
    \\textbf{{AI \\& Automation:}} ChatGPT, Claude, OpenAI, Microsoft Copilot, AI Workflow Acceleration, Python, Streamlit
    }}}}
\\end{{itemize}}
\\vspace{{-10pt}}

\\section{{Education}}
  \\resumeSubHeadingListStart
\\resumeSubheading
      {{M.S. Technology Management -- University of Illinois, Urbana Champaign}}{{\\textit{{Aug 2023 -- Aug 2024}}}}
      {{}}{{}}
      \\vspace{{-20pt}}
    \\resumeSubHeadingListEnd

\\end{{document}}
"""


def render_codex_prompt(result: dict[str, Any]) -> str:
    profile = result["jd_profile"]
    compact_result = {
        "jd_profile": {
            key: value
            for key, value in profile.items()
            if key
            in {
                "role_title",
                "role_family",
                "seniority",
                "core_competencies",
                "best_evidence",
                "keywords",
                "key_metrics",
                "must_show",
                "resume_strategy",
            }
        },
        "matches": result["matches"],
        "best_overall_points": all_ranked_points(result, limit=18),
    }
    return (
        "# Codex Resume Tailoring Task\n\n"
        "You are the intelligence layer for this resume tailoring product.\n\n"
        "## Instructions\n\n"
        "- Read the JD profile and matched experience evidence below.\n"
        "- Select the strongest bullets for the target role; do not blindly use every match.\n"
        "- Rewrite selected bullets into polished, final resume bullets.\n"
        "- Keep every claim truthful to the provided evidence.\n"
        "- Use metrics only when the metric placeholder contains a real number or explicit impact.\n"
        "- Do not invent employers, tools, numbers, outcomes, or responsibilities.\n"
        "- Prefer concise bullets with action, scope, tools/process, and business impact.\n"
        "- Return final bullets grouped by experience source.\n"
        "- Also include a short explanation of why these bullets fit the role.\n\n"
        "## Target JD Profile\n\n"
        f"```json\n{json.dumps(compact_result['jd_profile'], indent=2, ensure_ascii=False)}\n```\n\n"
        "## Best Overall Points\n\n"
        f"```json\n{json.dumps(compact_result['best_overall_points'], indent=2, ensure_ascii=False)}\n```\n\n"
        "## All Top Points By Experience\n\n"
        f"```json\n{json.dumps(compact_result['matches'], indent=2, ensure_ascii=False)}\n```\n"
    )


def write_product_package(result: dict[str, Any], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "01_jd_intelligence.md": render_jd_intelligence(result),
        "02_match_report.md": render_markdown(result),
        "03_codex_finalization_prompt.md": render_codex_prompt(result),
        "04_final_resume_bullets.md": render_final_workspace(result),
        "05_modified_points_only.md": render_modified_points_only(result),
        "06_final_resume_latex.tex": render_latex_resume(result),
        "match_data.json": json.dumps(result, indent=2, ensure_ascii=False),
    }
    written = []
    for file_name, content in files.items():
        path = output_dir / file_name
        path.write_text(content, encoding="utf-8")
        written.append(path)
    return written


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Match job descriptions against experience JSON point banks.",
        epilog=textwrap.dedent(
            """
            Examples:
              python resume_matcher.py --product
              python resume_matcher.py
              python resume_matcher.py --jd jd.txt
              python resume_matcher.py --jd jd.txt --top 3 --format md --output match.md
              python resume_matcher.py --jd jd.txt --format codex --output codex_prompt.md
              python resume_matcher.py --jd jd.txt --use-llm --model gpt-4.1-mini
            """
        ),
    )
    parser.add_argument(
        "--jd",
        default="job_description.txt",
        help="Path to a job description text file",
    )
    parser.add_argument(
        "--experiences",
        default="experiences",
        help="Folder containing experience JSON files",
    )
    parser.add_argument("--top", type=int, default=5, help="Top points per experience")
    parser.add_argument(
        "--format", choices=["json", "md", "codex"], default="json", help="Output format"
    )
    parser.add_argument("--output", help="Optional output path")
    parser.add_argument(
        "--product",
        action="store_true",
        help="Create the full intelligent tailoring package in outputs/latest",
    )
    parser.add_argument(
        "--output-dir",
        default="outputs/latest",
        help="Folder for --product output",
    )
    parser.add_argument("--use-llm", action="store_true", help="Use OpenAI for JD parsing and bullet adaptation")
    parser.add_argument("--model", default="gpt-4.1-mini", help="OpenAI model for --use-llm")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    jd_path = Path(args.jd)
    experience_dir = Path(args.experiences)

    if not jd_path.exists():
        raise FileNotFoundError(
            f"Job description file not found: {jd_path}\n"
            "Create it or run: notepad job_description.txt\n"
            "Then paste the job description and run this command again."
        )

    jd_text = jd_path.read_text(encoding="utf-8-sig")
    if not jd_text.strip() or "PASTE THE JOB DESCRIPTION BELOW" in jd_text:
        raise ValueError(
            f"{jd_path} is empty or still contains the template text.\n"
            "Paste the full job description into that file first."
        )
    experiences = load_experiences(experience_dir)
    if args.use_llm:
        jd_profile = extract_jd_profile_llm(jd_text, args.model)
    else:
        jd_profile = extract_jd_profile_heuristic(jd_text)

    result = match_experiences(
        experiences=experiences,
        jd_profile=jd_profile,
        top_n=args.top,
        use_llm=args.use_llm,
        model=args.model,
    )

    if args.product:
        written = write_product_package(result, Path(args.output_dir))
        print("Created intelligent resume tailoring package:")
        for path in written:
            print(f"- {path}")
        print("")
        print("Final resume:")
        print(f"- {Path(args.output_dir) / '06_final_resume_latex.tex'}")
        return 0

    if args.format == "md":
        rendered = render_markdown(result)
    elif args.format == "codex":
        rendered = render_codex_prompt(result)
    else:
        rendered = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
