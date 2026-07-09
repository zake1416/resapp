# Agentic Resume Tailoring Product

This is the new AI-agent workflow.

You paste a job description into `job_description.txt`, run one command, and Codex agents build the tailored resume from your experience JSONs.

## Main Workflow

```powershell
notepad job_description.txt
python agentic_resume.py
```

Final output:

```text
outputs/agentic/latest/04_final_resume.tex
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

## Legacy

`resume_matcher.py` is now legacy. Keep it only for deterministic debugging or comparison.
