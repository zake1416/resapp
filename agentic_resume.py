
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
from datetime import date
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_DIR = Path("outputs/agentic")
SKILL_CATEGORIES = ["Methods", "Operations", "Analytics", "Systems & Stack", "Tools"]
STRONG_ACTION_VERBS = {
    "Accelerated", "Activated", "Advanced", "Aligned", "Analyzed", "Architected", "Audited",
    "Balanced", "Built", "Centralized", "Clarified", "Connected", "Consolidated", "Controlled",
    "Converted", "Coordinated", "Created", "Defined", "Delivered", "Designed", "Detected",
    "Developed", "Diagnosed", "Directed", "Documented", "Drove", "Enabled", "Established",
    "Executed", "Expanded", "Facilitated", "Governed", "Guided", "Improved", "Integrated",
    "Launched", "Led", "Mapped", "Managed", "Measured", "Modernized", "Monitored", "Optimized",
    "Orchestrated", "Owned", "Prioritized", "Processed", "Produced", "Reconciled", "Reduced",
    "Refined", "Resolved", "Sequenced", "Shipped", "Simplified", "Standardized", "Strengthened",
    "Streamlined", "Supported", "Synthesized", "Tracked", "Translated", "Validated",
}
WEAK_BULLET_STARTS = {
    "Applied", "Assisted", "Contributed", "Helped", "Participated", "Performed", "Responsible",
    "Tasked", "Used", "Utilized", "Worked",
}

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

ROLE_FAMILY_ALIASES = {
    "ai_enablement": ["ai enablement analyst", "ai enablement", "enable ai", "ai adoption", "ai training"],
    "ai_operations": ["ai operations analyst", "ai operations", "ai ops", "agent operations", "model operations"],
    "ai_transformation": ["ai transformation analyst", "ai transformation", "agentic", "agentforce", "digital ai"],
    "product_operations": ["product operations analyst", "product operations", "product ops", "roadmap", "backlog", "launch"],
    "business_operations": ["business operations associate", "business operations", "bizops", "operating rhythm"],
    "strategy_operations": ["strategy & operations", "strategy and operations", "strategic operations", "business strategy"],
    "program": ["program analyst", "program coordinator", "project manager", "program manager", "pmo", "project"],
    "business_systems": ["business systems analyst", "business systems", "requirements", "uat", "systems analyst"],
    "customer_success_ops": ["customer success operations", "customer success ops", "customer operations"],
    "implementation": ["implementation analyst", "implementation", "onboarding", "go-live", "cutover", "deployment"],
    "solutions": ["solutions analyst", "solution analyst", "solutions", "client solution"],
    "gtm_operations": ["gtm operations", "go-to-market", "sales operations", "marketing operations"],
    "revenue_operations": ["revenue operations", "revops", "quote-to-cash", "lead-to-cash", "billing", "collections"],
    "process_improvement": ["process improvement", "continuous improvement", "lean", "six sigma", "bpi", "workflow"],
    "digital_transformation": ["digital transformation", "transformation", "systems transformation", "modernization"],
    "research_operations": ["research operations", "research", "survey", "market research"],
    "program_ai": ["program associate, ai", "ai program", "program associate ai"],
    "operations_ai": ["operations associate, ai", "operations associate ai", "ai operations associate"],
    "customer_value": ["customer value", "value analyst", "client value", "customer outcomes"],
}

EVIDENCE_TYPE_PATTERNS = {
    "ai_enablement": ["ai enablement", "ai fluency", "training", "agentforce", "responsible ai", "adoption"],
    "ai_operations": ["ai operations", "agent", "monitoring", "quality", "source content", "automation", "model"],
    "automation": ["automation", "automated", "agentforce", "einstein", "workflow automation", "manual work"],
    "product_roadmap": ["roadmap", "backlog", "feature", "launch", "product", "prioritization"],
    "business_operations": ["operating rhythm", "business operations", "cadence", "ownership", "capacity"],
    "strategy_planning": ["strategy", "strategic", "v2mom", "portfolio", "prioritization", "business case"],
    "program_governance": ["program", "project", "pmo", "governance", "milestone", "dependency", "deliverable"],
    "business_systems": ["requirements", "systems", "uat", "validation", "functional", "system"],
    "customer_success": ["customer success", "customer experience", "case deflection", "support friction"],
    "implementation": ["implementation", "go-live", "readiness", "deployment", "release", "cutover", "onboarding"],
    "solutions": ["solution", "client need", "platform capability", "requirements", "use case"],
    "gtm_operations": ["gtm", "go-to-market", "seller", "sales operations", "marketing", "campaign"],
    "revenue_operations": ["revenue operations", "billing", "collections", "quote-to-cash", "lead-to-cash", "cash flow", "aov"],
    "process_improvement": ["process improvement", "bpi", "workflow", "dmaic", "lean", "audit", "gap", "standardiz"],
    "digital_transformation": ["digital transformation", "erp", "marketing cloud", "revenue cloud", "migration", "transformation"],
    "research_operations": ["research", "survey", "analytics", "fraud detection", "respondent"],
    "customer_value": ["customer value", "client value", "retention", "adoption", "insight", "decision"],
    "analytics_reporting": ["dashboard", "reporting", "kpi", "metrics", "tableau", "excel", "insights"],
    "risk_mitigation": ["risk", "mitigation", "blocker", "issue", "escalation", "defect", "fraud", "continuity"],
    "compliance_controls": ["compliance", "sox", "control", "audit", "policy", "regulated"],
    "change_enablement": ["change", "enablement", "training", "adoption", "sponsor", "communications"],
    "stakeholder_management": ["stakeholder", "cross-functional", "executive", "sme", "leadership", "partner"],
    "data_quality": ["data quality", "data validation", "etl", "accuracy", "migration data", "integrity"],
    "client_facing": ["client", "customer-facing", "customer", "seller", "account executive"],
}

ALIGNMENT_TO_EVIDENCE = {
    "project_planning_execution": "program_governance",
    "enterprise_software_implementation": "implementation",
    "testing_release_readiness": "business_systems",
    "risk_mitigation": "risk_mitigation",
    "program_governance_compliance": "compliance_controls",
    "cross_functional_stakeholder_management": "stakeholder_management",
    "continuous_process_improvement": "process_improvement",
    "duplicate_reference_only": "duplicate_reference_only",
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


def canonical_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def weighted_term_hits(text: str, patterns: dict[str, list[str]]) -> dict[str, int]:
    lower = text.lower()
    hits: dict[str, int] = {}
    for key, needles in patterns.items():
        count = sum(1 for needle in needles if needle.lower() in lower)
        if count:
            hits[key] = count
    return hits


def infer_role_families_from_text(text: str) -> list[str]:
    hits = weighted_term_hits(text, ROLE_FAMILY_ALIASES)
    return [key for key, _ in sorted(hits.items(), key=lambda item: (-item[1], item[0]))]


def infer_evidence_types_from_text(text: str) -> list[str]:
    hits = weighted_term_hits(text, EVIDENCE_TYPE_PATTERNS)
    return [key for key, _ in sorted(hits.items(), key=lambda item: (-item[1], item[0]))]


def role_name_to_family(role_name: str) -> str | None:
    normalized = role_name.lower()
    for family, aliases in ROLE_FAMILY_ALIASES.items():
        if any(alias in normalized for alias in aliases):
            return family
    key = canonical_key(role_name)
    return key if key in ROLE_FAMILY_ALIASES else None


def selection_profile_from_point(
    point: dict[str, Any],
    tags: dict[str, Any],
    searchable: str,
    evidence_text: str,
) -> dict[str, Any]:
    explicit = point.get("selection_profile") or tags.get("selection_profile") or {}
    role_scores: dict[str, int] = {}

    for role in tags.get("best_fit_roles", []) or []:
        family = role_name_to_family(str(role))
        if family:
            role_scores[family] = max(role_scores.get(family, 0), 5)
    for role in tags.get("secondary_fit_roles", []) or []:
        family = role_name_to_family(str(role))
        if family:
            role_scores[family] = max(role_scores.get(family, 0), 3)
    role_hint_text = clean_text([
        point.get("point_title"),
        point.get("base_resume_point"),
        tags.get("best_fit_roles"),
        tags.get("secondary_fit_roles"),
    ])
    for family in infer_role_families_from_text(role_hint_text):
        role_scores[family] = max(role_scores.get(family, 0), 2)

    explicit_scores = explicit.get("role_family_scores", {}) if isinstance(explicit, dict) else {}
    if isinstance(explicit_scores, dict):
        for key, value in explicit_scores.items():
            family = canonical_key(str(key))
            try:
                score = int(value)
            except (TypeError, ValueError):
                continue
            role_scores[family] = max(role_scores.get(family, 0), score)

    evidence_types = infer_evidence_types_from_text(evidence_text)
    explicit_evidence = explicit.get("evidence_types", []) if isinstance(explicit, dict) else []
    evidence_types.extend(str(item) for item in explicit_evidence or [])
    evidence_types = unique([canonical_key(item) for item in evidence_types if item], 20)

    text = searchable.lower()
    strength = str(explicit.get("strength", "")).lower() if isinstance(explicit, dict) else ""
    if not strength:
        if any(term in text for term in ["$1m", "$180m", "$500k", "$120k", "50,000", "100%", "85%", "75%", "60%", "30%", "22%", "20%"]):
            strength = "high"
        elif point.get("duplicate_of") or "duplicate_reference_only" in evidence_types:
            strength = "duplicate"
        elif any(term in text for term in ["volunteer", "credential", "completed corporate training", "check-in"]):
            strength = "low"
        else:
            strength = "medium"

    resume_use = str(explicit.get("resume_use", "")).lower() if isinstance(explicit, dict) else ""
    if not resume_use:
        resume_use = "reference" if point.get("duplicate_of") else ("supporting" if strength == "low" else "primary")

    return {
        "role_family_scores": role_scores,
        "evidence_types": evidence_types,
        "strength": strength,
        "resume_use": resume_use,
    }


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")
    return slug or "resume"


def markdown_escape(value: Any) -> str:
    text = clean_text(value)
    return text.replace("|", "\\|").replace("\n", " ").strip()


def strip_leading_marker(text: str) -> str:
    return re.sub(r"^(?:(?:[^\x00-\x7F]+)|[^\w$])+\s*", "", text).strip()


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
        clean = strip_leading_marker(clean)
        if 4 <= len(clean.split()) <= 32:
            lower = clean.lower()
            if any(k in lower for k in [
                "connect", "visibility", "reduce", "single view", "governance", "ai", "automation",
                "adoption", "training", "templates", "partner", "workflow", "dashboard", "intake", "delivery",
                "planning", "roadmaps", "execution", "dependencies", "risks", "progress", "scope",
                "metrics", "exit criteria", "deliverables", "system", "inputs", "decisions", "outputs",
                "ambiguity", "v1", "pilot", "requirements", "documentation", "tradeoffs",
            ]):
                phrases.append(clean)
    return unique(phrases, 35)


def select_priority_jd_phrases(phrases: list[str], limit: int = 12) -> list[str]:
    """Prefer a diverse set of JD priorities instead of over-focusing on one repeated keyword."""
    priority_groups = [
        ["scope", "success metrics", "exit criteria", "deliverables", "operating cadence", "outcomes"],
        ["ambiguous", "ambiguity", "system", "inputs", "decisions", "outputs", "named owners"],
        ["prototype", "v1", "pilot", "usage feedback", "iterate"],
        ["cross-functional", "ownership", "dependency", "follow-through", "escalation"],
        ["communication", "decision memos", "narrative updates", "tradeoffs", "documentation"],
        ["adoption", "handoff", "buy-in", "path of least resistance"],
        ["analysis", "sql", "bi", "validate metrics", "data quality", "measure"],
        ["jira", "confluence", "dashboard", "repeatable cadence"],
    ]
    selected: list[str] = []
    lower_pairs = [(phrase, phrase.lower()) for phrase in phrases]
    for terms in priority_groups:
        for phrase, lower in lower_pairs:
            if phrase not in selected and any(term in lower for term in terms):
                selected.append(phrase)
                break
        if len(selected) >= limit:
            break
    for phrase in phrases:
        if len(selected) >= limit:
            break
        if phrase not in selected:
            selected.append(phrase)
    return unique(selected, limit)


def extract_jd_header(jd_text: str) -> dict[str, str]:
    header = {"company_name": "", "role_title": ""}
    lines = [line.strip() for line in jd_text.splitlines()[:30] if line.strip()]
    for line in lines:
        company = re.match(r"^(?:company|organization|employer|client)\s*:\s*(.+)$", line, flags=re.IGNORECASE)
        if company and not header["company_name"]:
            header["company_name"] = company.group(1).strip(" .-")
            continue
        role = re.match(r"^(?:job\s*)?(?:role|title|position)\s*:\s*(.+)$", line, flags=re.IGNORECASE)
        if role and not header["role_title"]:
            header["role_title"] = role.group(1).strip(" .-")
    return header


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
    header = extract_jd_header(jd_text)
    title = header["role_title"]
    for line in jd_text.splitlines()[:20]:
        if title:
            break
        if re.search(r"analyst|manager|associate|specialist|consultant|coordinator", line, re.IGNORECASE):
            title = line.strip(" -:")
            break
    company_name = header["company_name"]
    for line in jd_text.splitlines()[:30]:
        if company_name:
            break
        m = re.search(r"about\s+([A-Za-z0-9&.'-]+)", line, re.IGNORECASE)
        if m:
            company_name = m.group(1).strip(" .-")
            break
    priority_candidates = unique([
        phrase for phrase in phrases
        if any(term in phrase.lower() for term in [
            "connect", "intake", "delivery", "visibility", "single view", "reduce duplication",
            "manual effort", "governance", "ai", "automation", "adoption", "planning", "roadmaps",
            "execution tracking", "dependencies", "risks", "progress", "scope", "metrics",
            "exit criteria", "deliverables", "system", "inputs", "decisions", "outputs",
            "ambiguity", "v1", "pilot", "requirements", "documentation", "tradeoffs",
        ])
    ], 35)
    priority_phrases = select_priority_jd_phrases(priority_candidates, 12)
    role_families = infer_role_families_from_text(jd_text)
    target_evidence_types = infer_evidence_types_from_text(jd_text)
    return {
        "role_title": title,
        "company_name": company_name,
        "role_families": role_families[:6],
        "target_evidence_types": target_evidence_types[:10],
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
            tags.get("best_fit_roles"),
            tags.get("secondary_fit_roles"),
            tags.get("adaptation_direction"),
            tags.get("target_role_alignment"),
            point.get("selection_profile"),
        ])
        evidence_text = clean_text([
            point.get("point_title"),
            point.get("base_resume_point"),
            tags.get("evidence_proof"),
        ])
        selection_profile = selection_profile_from_point(point, tags, searchable, evidence_text)
        normalized.append({
            "id": point.get("id", ""),
            "legacy_id": point.get("legacy_id", ""),
            "duplicate_of": point.get("duplicate_of", ""),
            "point_title": point.get("point_title", ""),
            "base_resume_point": point.get("base_resume_point", ""),
            "core_competency": tags.get("core_competency", []),
            "functional_skill": tags.get("functional_skill", []),
            "business_outcome": tags.get("business_outcome", []),
            "evidence_proof": tags.get("evidence_proof", []),
            "metrics": extract_metrics(clean_text(tags.get("metric_placeholder", [])) + " " + searchable),
            "best_fit_roles": tags.get("best_fit_roles", []),
            "secondary_fit_roles": tags.get("secondary_fit_roles", []),
            "target_role_alignment": tags.get("target_role_alignment", []),
            "selection_profile": selection_profile,
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

    profile = point.get("selection_profile", {}) or {}
    role_scores = profile.get("role_family_scores", {}) or {}
    jd_role_families = jd_profile.get("role_families", []) or []
    matched_role_families = [
        family for family in jd_role_families
        if int(role_scores.get(family, 0) or 0) > 0
    ]
    for family in matched_role_families:
        score += min(5, int(role_scores.get(family, 0) or 0)) * 2.5

    point_evidence_types = profile.get("evidence_types", []) or []
    jd_evidence_types = jd_profile.get("target_evidence_types", []) or []
    matched_evidence_types = [
        evidence_type for evidence_type in jd_evidence_types
        if evidence_type in point_evidence_types
    ]
    score += len(matched_evidence_types) * 4

    strength = str(profile.get("strength", "")).lower()
    if strength == "high":
        score += 4
    elif strength == "low":
        score -= 5
    elif strength == "duplicate":
        score -= 8

    resume_use = str(profile.get("resume_use", "")).lower()
    if resume_use == "primary":
        score += 2
    elif resume_use == "supporting":
        score -= 2
    elif resume_use == "reference":
        score -= 10

    if point.get("duplicate_of"):
        score -= 12

    return {
        "score": round(score, 2),
        "matched_keywords": overlap[:20],
        "matched_core_competencies": unique(matched_competencies, 8),
        "matched_jd_phrases": unique(matched_phrases, 8),
        "matched_tools": unique(matched_tools, 8),
        "matched_role_families": unique(matched_role_families, 8),
        "matched_evidence_types": unique(matched_evidence_types, 10),
    }


def evidence_priority_for_jd(jd_profile: dict[str, Any]) -> list[str]:
    role_families = jd_profile.get("role_families", []) or []
    priorities = list(jd_profile.get("target_evidence_types", []) or [])
    role_defaults = {
        "ai_enablement": ["ai_enablement", "automation", "change_enablement", "stakeholder_management"],
        "ai_operations": ["ai_operations", "automation", "data_quality", "analytics_reporting"],
        "ai_transformation": ["ai_enablement", "digital_transformation", "automation", "strategy_planning"],
        "product_operations": ["product_roadmap", "program_governance", "analytics_reporting", "stakeholder_management"],
        "business_operations": ["business_operations", "process_improvement", "program_governance", "analytics_reporting"],
        "strategy_operations": ["strategy_planning", "analytics_reporting", "program_governance", "stakeholder_management"],
        "program": ["program_governance", "implementation", "risk_mitigation", "stakeholder_management"],
        "business_systems": ["business_systems", "implementation", "data_quality", "stakeholder_management"],
        "customer_success_ops": ["customer_success", "customer_value", "analytics_reporting", "process_improvement"],
        "implementation": ["implementation", "business_systems", "risk_mitigation", "change_enablement"],
        "solutions": ["solutions", "business_systems", "client_facing", "customer_value"],
        "gtm_operations": ["gtm_operations", "analytics_reporting", "stakeholder_management", "customer_value"],
        "revenue_operations": ["revenue_operations", "analytics_reporting", "process_improvement", "compliance_controls"],
        "process_improvement": ["process_improvement", "analytics_reporting", "implementation", "compliance_controls"],
        "digital_transformation": ["digital_transformation", "implementation", "automation", "change_enablement"],
        "research_operations": ["research_operations", "analytics_reporting", "data_quality", "customer_value"],
        "program_ai": ["ai_enablement", "program_governance", "automation", "change_enablement"],
        "operations_ai": ["ai_operations", "business_operations", "automation", "process_improvement"],
        "customer_value": ["customer_value", "client_facing", "analytics_reporting", "customer_success"],
    }
    for family in role_families:
        priorities.extend(role_defaults.get(family, []))
    priorities.extend(["stakeholder_management", "analytics_reporting", "process_improvement"])
    return unique(priorities, 10)


def select_balanced_points(scored: list[dict[str, Any]], count: int, jd_profile: dict[str, Any]) -> list[dict[str, Any]]:
    if count <= 0:
        return []
    candidates = sorted(scored, key=lambda p: p["score"], reverse=True)
    selected: list[dict[str, Any]] = []
    selected_ids: set[str] = set()
    selected_canonicals: set[str] = set()

    def canonical_id(point: dict[str, Any]) -> str:
        return str(point.get("duplicate_of") or point.get("id") or "")

    def can_take(point: dict[str, Any]) -> bool:
        point_id = str(point.get("id", ""))
        canonical = canonical_id(point)
        if point_id in selected_ids or canonical in selected_canonicals:
            return False
        if point.get("duplicate_of") and len([p for p in candidates if p.get("id") == point.get("duplicate_of")]) > 0:
            return False
        return True

    def take(point: dict[str, Any]) -> None:
        selected.append(point)
        selected_ids.add(str(point.get("id", "")))
        selected_canonicals.add(canonical_id(point))

    for evidence_type in evidence_priority_for_jd(jd_profile):
        if len(selected) >= count:
            break
        options = [
            point for point in candidates
            if can_take(point) and evidence_type in (point.get("selection_profile", {}).get("evidence_types", []) or [])
        ]
        if options:
            take(options[0])

    for point in candidates:
        if len(selected) >= count:
            break
        if can_take(point):
            take(point)

    if len(selected) < count:
        for point in candidates:
            if len(selected) >= count:
                break
            if str(point.get("id", "")) not in selected_ids:
                take(point)

    return selected[:count]


def select_evidence(jd_profile: dict[str, Any], experience_dir: Path) -> dict[str, Any]:
    selected: list[dict[str, Any]] = []
    for config in EXPERIENCES:
        scored = []
        for point in load_experience_points(experience_dir, config):
            score = score_point(point, jd_profile)
            scored.append({**point, **score})
        scored.sort(key=lambda p: p["score"], reverse=True)
        chosen = select_balanced_points(scored, config["count"], jd_profile)
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


def point_selection_reason(point: dict[str, Any]) -> str:
    reasons: list[str] = []
    if point.get("matched_core_competencies"):
        reasons.append("matches core competencies: " + ", ".join(map(str, point["matched_core_competencies"][:3])))
    if point.get("matched_evidence_types"):
        reasons.append("covers evidence types: " + ", ".join(map(str, point["matched_evidence_types"][:3])))
    if point.get("matched_role_families"):
        reasons.append("fits role family: " + ", ".join(map(str, point["matched_role_families"][:2])))
    if point.get("matched_tools"):
        reasons.append("proves requested tools: " + ", ".join(map(str, point["matched_tools"][:3])))
    if point.get("metrics"):
        reasons.append("has proof/metrics: " + ", ".join(map(str, point["metrics"][:3])))
    if point.get("duplicate_of"):
        reasons.append(f"reference duplicate of {point['duplicate_of']}")
    return "; ".join(reasons) or "selected as the strongest available transferable evidence for this experience"


def render_evidence_markdown(jd_profile: dict[str, Any], selected_evidence: dict[str, Any]) -> str:
    company = jd_profile.get("company_name") or "Company not provided"
    role = jd_profile.get("role_title") or "Role not provided"
    lines = [
        f"# Evidence Rationale - {markdown_escape(company)} / {markdown_escape(role)}",
        "",
        "This file explains which source points were selected for the tailored resume and why they fit the job description.",
        "",
        "## JD Signals",
        "",
        f"- Company: {markdown_escape(company)}",
        f"- Role: {markdown_escape(role)}",
        f"- Role families: {markdown_escape(', '.join(jd_profile.get('role_families', []) or [])) or 'None detected'}",
        f"- Evidence priorities: {markdown_escape(', '.join(evidence_priority_for_jd(jd_profile))) or 'None detected'}",
        f"- Required tools found in JD: {markdown_escape(', '.join(jd_profile.get('required_tools_keywords', []) or [])) or 'None detected'}",
        "",
    ]
    priorities = jd_profile.get("priority_jd_responsibilities", []) or []
    if priorities:
        lines.extend(["## Priority JD Responsibilities", ""])
        lines.extend([f"- {markdown_escape(item)}" for item in priorities[:10]])
        lines.append("")

    for exp in selected_evidence.get("experiences", []) or []:
        lines.extend([
            f"## {markdown_escape(exp.get('company'))} - {markdown_escape(exp.get('title'))}",
            "",
            "| ID | Score | Point Title | Why selected | Resume source point |",
            "|---|---:|---|---|---|",
        ])
        for point in exp.get("selected_points", []) or []:
            lines.append(
                "| "
                + " | ".join([
                    markdown_escape(point.get("id")),
                    markdown_escape(point.get("score")),
                    markdown_escape(point.get("point_title")),
                    markdown_escape(point_selection_reason(point)),
                    markdown_escape(point.get("base_resume_point")),
                ])
                + " |"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"



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


def normalized_terms(text: str) -> set[str]:
    weak_terms = STOPWORDS | {
        "improved", "aligned", "created", "built", "managed", "led", "drove", "used",
        "through", "across", "support", "supporting", "business", "operations",
    }
    return {token for token in tokens(text) if token not in weak_terms and len(token) > 3}


def starts_with_strong_action(text: str) -> bool:
    first = re.match(r"^\s*([A-Za-z]+)", text or "")
    if not first:
        return False
    verb = first.group(1)
    return verb in STRONG_ACTION_VERBS and verb not in WEAK_BULLET_STARTS


def quantification_profile(bullets: list[str]) -> dict[str, int]:
    profile = {"percent": 0, "money": 0, "count": 0, "scope": 0}
    scope_terms = [
        "team", "teams", "department", "departments", "stakeholder", "stakeholders",
        "workflow", "workflows", "project", "projects", "platform", "platforms",
        "client", "clients", "control", "controls", "report", "reports", "sprint", "sprints",
    ]
    for bullet in bullets:
        lower = bullet.lower()
        if re.search(r"\b\d+(?:\.\d+)?%", bullet):
            profile["percent"] += 1
        if re.search(r"\$\d", bullet):
            profile["money"] += 1
        if re.search(r"\b\d+\+?\s?(?:projects|apps|applications|teams|stakeholders|workflows|dashboards|articles|cases|clients|users|reports|sprints|initiatives|pages|risks|departments|controls)\b", bullet, re.IGNORECASE):
            profile["count"] += 1
        if any(term in lower for term in scope_terms):
            profile["scope"] += 1
    return profile


def quality_issues(content: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    bullets: list[tuple[str, int, str]] = []
    for exp in content.get("experiences", []) or []:
        key = str(exp.get("key", "experience"))
        for index, bullet in enumerate(exp.get("bullets", []) or [], start=1):
            bullets.append((key, index, str(bullet)))

    awkward_phrases = [
        "adoption handoffs",
        "adoption potential",
        "handoff durability",
        "without adding informal follow-up burden",
        "daily execution across departments for teams",
        "decision-making behaviors, and relationships",
    ]
    for key, index, bullet in bullets:
        lower = bullet.lower()
        if not starts_with_strong_action(bullet):
            first = re.match(r"^\s*([A-Za-z]+)", bullet or "")
            verb = first.group(1) if first else "unknown"
            issues.append(f"{key} bullet {index} should start with a stronger action verb; found '{verb}'.")
        for phrase in awkward_phrases:
            if phrase in lower:
                issues.append(f"{key} bullet {index} contains awkward phrase: {phrase}.")

    repeated_terms = ["adoption", "handoff", "workflow", "governance", "alignment"]
    for term in repeated_terms:
        count = sum(1 for _, _, bullet in bullets if re.search(rf"\b{re.escape(term)}\w*\b", bullet, re.IGNORECASE))
        limit = 3 if term in {"adoption", "workflow", "governance"} else 2
        if count > limit:
            issues.append(f"Resume repeats '{term}' in {count} bullets; reduce keyword stuffing.")

    for i, (key_a, index_a, bullet_a) in enumerate(bullets):
        terms_a = normalized_terms(bullet_a)
        if len(terms_a) < 4:
            continue
        for key_b, index_b, bullet_b in bullets[i + 1:]:
            terms_b = normalized_terms(bullet_b)
            if len(terms_b) < 4:
                continue
            overlap = terms_a & terms_b
            similarity = len(overlap) / max(1, min(len(terms_a), len(terms_b)))
            if similarity >= 0.58:
                issues.append(
                    f"{key_a} bullet {index_a} is too similar to {key_b} bullet {index_b}; "
                    f"shared terms: {', '.join(sorted(overlap)[:6])}."
                )

    bullet_texts = [bullet for _, _, bullet in bullets]
    quant = quantification_profile(bullet_texts)
    if bullet_texts and quant["percent"] > 0 and quant["money"] + quant["count"] + quant["scope"] <= quant["percent"]:
        issues.append("Quantification relies too heavily on percentages; add dollar, count, scale, scope, or business-impact context from evidence.")
    if bullet_texts and quant["money"] + quant["count"] + quant["scope"] < 4:
        issues.append("Resume needs more non-percentage impact context such as dollar value, counts, teams, projects, workflows, controls, or platforms.")

    skills = content.get("skills", {}) or {}
    for category in SKILL_CATEGORIES:
        items = list(skills.get(category, []) or [])
        line = f"{category}: {', '.join(map(str, items))}"
        if len(line) > 112:
            issues.append(f"Skills category {category} is too long for one line; shorten skill names.")
        long_items = [str(item) for item in items if len(str(item)) > 28]
        if long_items:
            issues.append(f"Skills category {category} has overly long skill labels: {', '.join(long_items[:3])}.")
    return issues


def normalize_skill_values(values: Any, limit: int = 5) -> list[str]:
    if not isinstance(values, list):
        return []
    cleaned = []
    for value in values:
        text = re.sub(r"\s+", " ", str(value)).strip(" ,;")
        if text:
            cleaned.append(text)
    return unique(cleaned, limit)


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
- Start every bullet with a strong action verb. Avoid weak starts like Applied, Used, Utilized, Helped, Assisted, Responsible for, Worked on, or Performed.
- Use varied verbs across the resume; do not start many bullets with the same verb.

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
- For direct JD bullets, mirror a diverse responsibility mix: scope/metrics/exit criteria, system inputs and owners, v1 launch/pilots, cross-functional execution, executive documentation, analysis/data quality, adoption/handoff, operating cadence.
- Do not force the same JD phrase into multiple experiences. Across the whole resume, use "adoption" in at most 3 bullets and "handoff" in at most 2 bullets.
- Do not write phrases like "Led HubSpot Automation" unless selected evidence explicitly proves HubSpot. Use "strengthened CRM automation workflows" or "improved lead-management operating cadence" instead.

Strict rules:
- Summary must be 45 words or fewer and use JD language.
- No Projects section.
- No placeholders.
- Do not claim direct ownership/use of JD tools unless selected evidence explicitly proves that tool. This includes HubSpot, ServiceNow, Power BI, ZoomInfo, Cvent, GA4, Monday.com, ON24, SAP, location, W2, visa, or certifications.
- If a priority JD responsibility contains an unsupported tool such as HubSpot, translate it truthfully into transferable language: CRM automation, lead-management workflows, lifecycle-stage governance, audience/list logic, reporting, data quality, handoffs, integrations, and revenue operations.
- You may use transferable language such as dashboards, reporting, workflow automation, intake-to-delivery visibility, tool adoption, governance, CRM processes, lifecycle stages, lead routing, and execution tracking when evidence supports it.
- Prefer real metrics from evidence: dollar values, counts, teams, workflows, projects, articles, apps, controls, platforms, and percentages.
- Quantification must not be only percentages. Add high-impact context such as scale, volume, dollar value, number of projects/teams/workflows/controls, risk reduction, customer impact, compliance impact, or decision speed when evidence supports it.
- Every bullet should visibly connect to at least one JD responsibility or core competency.
- Every bullet must have a distinct main idea. Do not create multiple bullets that all say adoption, handoff, governance, alignment, or workflow in different words.
- Avoid awkward AI phrases and noun piles such as "adoption handoffs", "adoption potential", "handoff durability", "daily execution across departments for teams", or "decision-making behaviors and relationships".
- Use plain resume language. If a phrase sounds like a copied JD keyword cluster, rewrite it around the actual evidence.
- Job titles in the LaTeX are intentionally functional/JD-aligned titles reflecting actual work, not necessarily HR-paper titles.
- Skills must sound like a human resume, not an AI-generated taxonomy.
- Use exactly five plain category names: Methods, Operations, Analytics, Systems & Stack, Tools.
- Put exactly five skills in each category.
- Keep each skill category compact enough to fit on one resume line; use short labels, not long phrases.
- Skills should be specific and defensible from evidence. Avoid vague phrases like "enterprise AI", "strategic transformation", or "stakeholder excellence" unless the JD/evidence directly supports them.
- Prioritize tools, methodologies, platforms, and stack language mentioned in the JD when the selected evidence supports them.
- If a JD tool is not proven by selected evidence, do not list it directly; use truthful transferable stack language instead.
- Tools should be software/platform names only. Methods should be ways of working. Operations should be business/system domains. Analytics should be reporting, data, testing, and measurement skills. Systems & Stack should capture supported business systems, SaaS/GTM/revenue stack, CRM, PLG, AI workflow, and implementation-stack concepts.

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
    "Methods": [],
    "Operations": [],
    "Analytics": [],
    "Systems & Stack": [],
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
Preserve the JD-direct bullet rules: Salesforce first 2, MarketMaker PM first 2, and first bullet for all remaining experiences must start from priority JD responsibilities, using a diverse mix of responsibilities instead of repeating adoption/handoff.
Fix repeated wording, overlapping bullets, and awkward AI phrases. Across the whole resume, use "adoption" in at most 3 bullets and "handoff" in at most 2 bullets.
Every bullet must start with a strong action verb. Avoid weak starts like Applied, Used, Utilized, Helped, Assisted, Responsible for, Worked on, or Performed.
Quantification must include high-impact context beyond percentages when evidence supports it: dollar values, counts, scale, teams, projects, workflows, controls, platforms, risk, compliance, or customer impact.
Remove any unsupported direct tool claims flagged in validation. If HubSpot or another JD tool is unsupported by selected evidence, convert it to truthful transferable language such as CRM automation, lead routing, lifecycle workflows, reporting, data quality, integrations, or revenue operations.
Keep skills in exactly five human resume categories only: Methods, Operations, Analytics, Systems & Stack, Tools. Keep exactly five items per category. Keep each category line compact enough to fit on one resume line.

VALIDATION ISSUES:
{json.dumps(rule_check, indent=2, ensure_ascii=False)}

JD PROFILE:
{json.dumps(jd_profile, indent=2, ensure_ascii=False)}

SELECTED EVIDENCE:
{json.dumps(selected_evidence, indent=2, ensure_ascii=False)}

CURRENT RESUME JSON:
{json.dumps(resume_content, indent=2, ensure_ascii=False)}
"""


def feedback_prompt(
    jd_profile: dict[str, Any],
    selected_evidence: dict[str, Any],
    resume_content: dict[str, Any],
    feedback: str,
) -> str:
    return f"""
Revise this resume JSON using the user's feedback. Return ONLY valid JSON in the same shape.

Use the same selected evidence. Do not invent claims, employers, tools, metrics, certifications, or dates.
Keep the resume truthful, concise, and ATS-friendly.
Implement the user's requested changes unless they conflict with evidence or resume quality.
If feedback asks for stronger alignment, use the JD profile and selected evidence to improve wording.
If feedback asks to remove something, remove or replace it with a defensible evidence-backed point.
Preserve required bullet counts unless the user explicitly asks for a different count.
Keep summary at 45 words or fewer.
Keep skills in exactly five categories: Methods, Operations, Analytics, Systems & Stack, Tools.
Keep exactly five items per skill category.
Keep each skill category compact enough to fit on one resume line; use concise labels.
Every bullet must start with a strong action verb. Avoid weak starts like Applied, Used, Utilized, Helped, Assisted, Responsible for, Worked on, or Performed.
Quantification must include high-impact context beyond percentages when evidence supports it: dollar values, counts, scale, teams, projects, workflows, controls, platforms, risk, compliance, or customer impact.
Avoid repeated wording, awkward AI phrases, and keyword stuffing.

USER FEEDBACK:
{feedback.strip()}

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
    raw_skills = content.get("skills") or {}
    operations = list(raw_skills.get("Operations", []) or raw_skills.get("Systems, Workflow & Governance", []) or [])
    systems_stack = list(raw_skills.get("Systems & Stack", []) or [])
    skills = {
        "Methods": normalize_skill_values(raw_skills.get("Methods", []) or raw_skills.get("Product, PMO & Stakeholder Operations", [])),
        "Operations": normalize_skill_values(operations),
        "Analytics": normalize_skill_values(raw_skills.get("Analytics", []) or raw_skills.get("Analytics & Reporting", [])),
        "Systems & Stack": normalize_skill_values(systems_stack or operations),
        "Tools": normalize_skill_values(raw_skills.get("Tools", [])),
    }
    if not skills["Operations"] and raw_skills.get("Enterprise AI & Automation"):
        skills["Operations"] = normalize_skill_values(raw_skills.get("Enterprise AI & Automation", []))
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
    issues.extend(quality_issues(content))
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
    skills = content.get("skills", {}) or {}
    for category in SKILL_CATEGORIES:
        items = skills.get(category, []) or []
        if len(items) != 5:
            issues.append(f"Skills category {category} has {len(items)} items; required 5.")
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
        r"    \small +1 217-607-7336 ~ ",
        r"    \href{mailto:aishwarya7uiuc@gmail.com}{aishwarya7uiuc@gmail.com} ~ ",
        r"    \href{https://linkedin.com/in/aishwarya-chourasia-65b381151/}{LinkedIn} ~",
        r"    \href{https://aishwarya2510.github.io/portfolio_new/}{Portfolio}",
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
        after_space = r"\vspace{-12pt}" if str(exp.get("key", "")) == "marketmaker_pm" else r"\vspace{-2pt}"
        lines.extend([
            r"\resumeSubheading",
            f"{{{latex_escape(company)}}}{{{latex_escape(location)}}}",
            f"{{{latex_escape(exp['title'])}}}{{{latex_escape(exp['dates'])}}}",
            r"\resumeItemListStart",
            *render_items(exp.get("bullets", [])),
            r"\resumeItemListEnd",
            "",
            after_space,
            "",
        ])
    lines.extend([
        r"\resumeSubHeadingListEnd",
        r"\vspace{-10pt}",
        r"\section{Skills}",
        r"\begin{itemize}[leftmargin=0.0in, label={}]",
        r"    \small{\item{",
        *[skill_line(label) for label in SKILL_CATEGORIES[:-1]],
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


def compile_pdf(tex_path: Path) -> Path:
    if not tex_path.exists():
        raise FileNotFoundError(f"Missing LaTeX file: {tex_path}")
    resolved = shutil.which("pdflatex")
    if not resolved:
        raise RuntimeError("pdflatex was not found. Install MiKTeX/TeX Live or compile the .tex manually.")
    completed = subprocess.run(
        [
            resolved,
            "-interaction=nonstopmode",
            "-halt-on-error",
            tex_path.name,
        ],
        cwd=str(tex_path.parent),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    write_text(tex_path.parent / "latex_compile.log", "\n".join([
        "STDOUT:",
        completed.stdout,
        "STDERR:",
        completed.stderr,
    ]))
    if completed.returncode != 0:
        raise RuntimeError(f"PDF compile failed. See {tex_path.parent / 'latex_compile.log'}")
    return tex_path.with_suffix(".pdf")


def build_output_dir(base_output_dir: Path, jd_profile: dict[str, Any], run_date: str | None = None) -> Path:
    run_date = run_date or date.today().isoformat()
    company = jd_profile.get("company_name") or "company_not_provided"
    role = jd_profile.get("role_title") or "role_not_provided"
    run_name = slugify("_".join([company, role]))
    return base_output_dir / run_date / run_name


def run_pipeline(args: argparse.Namespace) -> list[AgentResult]:
    base_output_dir = Path(args.output_dir)
    base_output_dir.mkdir(parents=True, exist_ok=True)

    jd_text = read_text(Path(args.jd))
    if not jd_text.strip():
        raise ValueError(f"Job description is empty: {args.jd}")

    jd_profile = analyze_jd(jd_text)
    output_dir = build_output_dir(base_output_dir, jd_profile, args.run_date)
    if output_dir.exists() and not args.no_clean:
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_text(output_dir / "input_job_description.txt", jd_text)
    write_text(output_dir / "01_jd_profile.json", json.dumps(jd_profile, indent=2, ensure_ascii=False))

    selected = select_evidence(jd_profile, Path(args.experiences))
    write_text(output_dir / "02_selected_evidence.json", json.dumps(selected, indent=2, ensure_ascii=False))
    write_text(output_dir / "02b_evidence_rationale.md", render_evidence_markdown(jd_profile, selected))

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
    if getattr(args, "compile_pdf", False):
        compile_pdf(output_dir / "04_final_resume.tex")
    args.resolved_output_dir = output_dir
    return results


def read_feedback(args: argparse.Namespace) -> str:
    parts: list[str] = []
    if args.feedback:
        parts.append(str(args.feedback))
    if args.feedback_file:
        parts.append(read_text(Path(args.feedback_file)))
    feedback = "\n\n".join(part.strip() for part in parts if part and part.strip()).strip()
    if not feedback:
        raise ValueError("Feedback mode needs --feedback or --feedback-file.")
    return feedback


def run_feedback_revision(args: argparse.Namespace) -> list[AgentResult]:
    if not args.resume_dir:
        raise ValueError("Feedback mode needs --resume-dir pointing to the generated resume folder.")
    output_dir = Path(args.resume_dir)
    required = [
        output_dir / "01_jd_profile.json",
        output_dir / "02_selected_evidence.json",
        output_dir / "03_resume_content.json",
    ]
    missing = [path for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError("Feedback mode is missing required files: " + ", ".join(map(str, missing)))

    feedback = read_feedback(args)
    write_text(output_dir / "feedback_latest.txt", feedback)

    jd_profile = json.loads(read_text(output_dir / "01_jd_profile.json"))
    selected = json.loads(read_text(output_dir / "02_selected_evidence.json"))
    content = normalize_resume_content(json.loads(read_text(output_dir / "03_resume_content.json")), jd_profile)
    unsupported_tools = unsupported_jd_tools(jd_profile, selected)

    results: list[AgentResult] = []
    revision = run_codex_json(
        "06_feedback_revision",
        feedback_prompt(jd_profile, selected, content, feedback),
        output_dir / "03_resume_content.json",
        output_dir,
        args.model,
    )
    results.append(revision)
    content = normalize_resume_content(json.loads(read_text(revision.output_path)), jd_profile)
    write_text(revision.output_path, json.dumps(content, indent=2, ensure_ascii=False))

    check = validate(content, unsupported_tools)
    write_text(output_dir / "05_rule_check.json", json.dumps(check, indent=2, ensure_ascii=False))
    for attempt in range(args.revision_attempts):
        if check["status"] == "pass":
            break
        followup = run_codex_json(
            f"06b_feedback_rule_fix_{attempt + 1}",
            revision_prompt(jd_profile, selected, content, check),
            output_dir / "03_resume_content.json",
            output_dir,
            args.model,
        )
        results.append(followup)
        content = normalize_resume_content(json.loads(read_text(followup.output_path)), jd_profile)
        write_text(followup.output_path, json.dumps(content, indent=2, ensure_ascii=False))
        check = validate(content, unsupported_tools)
        write_text(output_dir / "05_rule_check.json", json.dumps(check, indent=2, ensure_ascii=False))

    write_text(output_dir / "04_final_resume.tex", render_latex(content))
    pdf_path = compile_pdf(output_dir / "04_final_resume.tex")
    args.resolved_output_dir = output_dir
    args.resolved_pdf_path = pdf_path
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a tailored LaTeX resume from a JD and experience JSONs.")
    parser.add_argument("--jd", default="job_description.txt")
    parser.add_argument("--experiences", default="experiences")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR))
    parser.add_argument("--model", default=None)
    parser.add_argument("--revision-attempts", type=int, default=2)
    parser.add_argument("--no-clean", action="store_true")
    parser.add_argument("--run-date", default=None, help="Date folder for this application run, default YYYY-MM-DD today.")
    parser.add_argument("--compile-pdf", action="store_true", help="Compile the generated LaTeX resume to PDF.")
    parser.add_argument("--resume-dir", default=None, help="Existing generated resume folder to revise with feedback.")
    parser.add_argument("--feedback", default=None, help="Feedback text to apply to an existing generated resume.")
    parser.add_argument("--feedback-file", default=None, help="Path to a text file containing feedback to apply.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.resume_dir or args.feedback or args.feedback_file:
        results = run_feedback_revision(args)
    else:
        results = run_pipeline(args)
    resolved_dir = getattr(args, "resolved_output_dir", Path(args.output_dir))
    print("Resume pipeline complete:")
    for result in results:
        print(f"- {result.name}: {result.output_path}")
    print(f"- evidence_rationale: {resolved_dir / '02b_evidence_rationale.md'}")
    print(f"- rule_check: {resolved_dir / '05_rule_check.json'}")
    print(f"- final_resume: {resolved_dir / '04_final_resume.tex'}")
    pdf_path = getattr(args, "resolved_pdf_path", None)
    if pdf_path:
        print(f"- final_pdf: {pdf_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)




