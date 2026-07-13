# Agentic Resume Tailoring Product

This is the new AI-agent workflow.

You paste a job description into `job_description.txt`, run one command, and Codex agents build the tailored resume from your experience JSONs.

## First-Time Setup

New machine or new collaborator? Start with [`SETUP.md`](SETUP.md) for Python, Codex CLI, authentication, and troubleshooting instructions.

## Main Workflow

```powershell
notepad job_description.txt
python agentic_resume.py
```

Final output:

```text
outputs/agentic/latest/04_final_resume.tex
```

To also compile a PDF:

```powershell
python agentic_resume.py --compile-pdf
```

QA report:

```text
outputs/agentic/latest/05_qa_report.json
```

## Agent Pipeline

The system runs five Codex agents:

1. `01_jd_intelligence_agent`
   Extracts role title, company context, day-to-day responsibilities, core competencies, tools, keywords, reusable JD phrases, evidence needs, metrics, and things not to fake.

2. `02_evidence_mapping_agent`
   Reads every JSON in `experiences/` and maps the JD requirements to truthful evidence.

3. `03_resume_writing_agent`
   Writes the summary, experience bullets, skills, and alignment notes using the JD language plus your evidence.

4. `04_latex_build_agent`
   Converts the structured resume content into the final LaTeX resume.

5. `05_qa_agent`
   Reviews alignment, honesty, bullet counts, summary length, unsupported claims, and LaTeX risks.

## Generated Files

```text
outputs/agentic/latest/
  input_job_description.txt
  01_jd_profile.json
  02_evidence_map.json
  03_resume_content.json
  04_final_resume.tex
  05_qa_report.json
  prompts/
  raw/
  logs/
```

The `prompts/`, `raw/`, and `logs/` folders make the process inspectable. If an agent produces something wrong, you can see exactly what it was asked and what it answered.

## Resume Quality Rules

Every generated resume, including feedback revisions, is checked for:

- Strong action verbs at the start of every bullet
- Distinct bullets without repeated keyword stuffing
- High-impact quantification beyond percentages, such as dollars, counts, teams, projects, workflows, controls, platforms, risk, compliance, or customer impact
- Compact skill categories that fit cleanly on one resume line
- Truthful claims grounded in the selected evidence

## Why This Replaces The Old System

The old `resume_matcher.py` was mostly deterministic scoring and templating. It could move fast, but it could also feel fake because it was not deeply rethinking the JD.

The new `agentic_resume.py` uses Codex agents for the judgment-heavy work:

- JD extraction
- evidence reasoning
- bullet writing
- LaTeX generation
- QA

## Options

Use a different JD file:

```powershell
python agentic_resume.py --jd path\to\jd.txt
```

Use a different output folder:

```powershell
python agentic_resume.py --output-dir outputs/agentic/revenue_ops_homestyle
```

Pass a Codex model:

```powershell
python agentic_resume.py --model gpt-5
```

Keep existing output folder contents:

```powershell
python agentic_resume.py --no-clean
```

## Feedback Loop

After a resume is generated, give feedback against the generated folder. The script revises the structured resume JSON, re-renders LaTeX, runs validation, and compiles the final PDF.

```powershell
python agentic_resume.py `
  --resume-dir outputs\agentic\2026-07-13\carmax_business_operations_associate `
  --feedback "Remove advanced PC wording, make Salesforce less compliance-heavy, and make bullets sound more natural."
```

For longer feedback, put notes in a text file:

```powershell
notepad feedback.txt
python agentic_resume.py `
  --resume-dir outputs\agentic\2026-07-13\carmax_business_operations_associate `
  --feedback-file feedback.txt
```

Feedback outputs update these files in the same folder:

```text
03_resume_content.json
04_final_resume.tex
04_final_resume.pdf
05_rule_check.json
feedback_latest.txt
```

## Interactive Workflow Studio

Run the local visual workflow UI:

```powershell
python resume_workflow_server.py
```

Open:

```text
http://127.0.0.1:8765
```

The studio gives you a simple n8n/NiFi-style flow:

- Paste job description
- Run the agentic resume workflow
- Open generated LaTeX/PDF
- Paste feedback
- Regenerate final LaTeX/PDF

Generated UI runs are stored under:

```text
outputs/agentic_ui/
```

## Legacy

`resume_matcher.py` is now legacy. Keep it only for deterministic debugging or comparison.
