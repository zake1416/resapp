# Setup Guide

Use this guide when setting up the resume tailoring project on a new machine.

## What You Need

- Git
- Python 3.11 or newer
- OpenAI Codex CLI installed and authenticated
- Optional: a LaTeX distribution if you want to compile the generated `.tex` file into a PDF

This project is currently designed for Windows PowerShell, but the Python scripts use mostly standard-library code and can run on macOS or Linux with small path adjustments.

## 1. Clone The Repo

```powershell
git clone https://github.com/zake1416/resapp.git
cd resapp
```

If you already have the folder locally:

```powershell
cd C:\Users\Abhishek\Downloads\resapp
git pull
```

## 2. Create A Python Virtual Environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python --version
```

There is no required package install for the main `agentic_resume.py` flow right now; it uses Python standard-library modules.

If PowerShell blocks virtualenv activation, run:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

## 3. Install And Sign In To Codex

The main workflow calls the Codex CLI from Python. Codex must be available either on `PATH` as `codex`, or at this Windows location:

```text
%LOCALAPPDATA%\Programs\OpenAI\Codex\bin\codex.exe
```

Check whether Codex is installed:

```powershell
codex --version
codex doctor
```

Sign in:

```powershell
codex login
```

Codex supports ChatGPT sign-in and API-key sign-in for local CLI workflows. ChatGPT sign-in is the usual path for an interactive local setup; API-key sign-in is useful for automation.

Never commit Codex credentials or API keys. Codex may store local auth under `~\.codex\auth.json` or in the operating-system credential store.

## 4. Confirm Project Files

The important inputs are:

```text
job_description.txt
experiences/
  salesforce.json
  mmrcePM.json
  mmrceBA.json
  vista.json
  lti.json
```

`job_description.txt` is the active target job description. The JSON files in `experiences/` are the evidence bank. Keep resume claims truthful to those evidence files.

## 5. Run The Main Resume Workflow

Paste a job description into:

```text
job_description.txt
```

Then run:

```powershell
python agentic_resume.py
```

Optional examples:

```powershell
python agentic_resume.py --jd job_description.txt
python agentic_resume.py --output-dir outputs/agentic/financial_operations_processor
python agentic_resume.py --model gpt-5
python agentic_resume.py --no-clean
```

## 6. Review The Outputs

The generated run folder is under:

```text
outputs/agentic/
```

Key files:

```text
01_jd_profile.json
02_selected_evidence.json
03_resume_content.json
04_final_resume.tex
05_rule_check.json
prompts/
raw/
logs/
```

Start with:

```text
04_final_resume.tex
05_rule_check.json
```

If the output looks wrong, inspect `prompts/`, `raw/`, and `logs/` to see exactly what Codex received and returned.

## 7. Optional: Compile The LaTeX Resume

Install a LaTeX distribution such as MiKTeX or TeX Live. Then run:

```powershell
pdflatex outputs\agentic\latest\04_final_resume.tex
```

If the output folder is not `latest`, replace the path with the actual generated folder.

## 8. Legacy Workflow

`resume_matcher.py` is the older deterministic workflow. Use it only for debugging, comparison, or generating intermediate match reports.

Examples:

```powershell
python resume_matcher.py --product
python resume_matcher.py --jd job_description.txt --format md --output match_report.md
python resume_matcher.py --jd job_description.txt --format codex --output codex_prompt.md
```

The legacy LLM option uses the OpenAI API directly and requires `OPENAI_API_KEY`:

```powershell
$env:OPENAI_API_KEY = "your-api-key"
python resume_matcher.py --jd job_description.txt --use-llm --model gpt-4.1-mini
```

Do not save real API keys in committed files.

## Troubleshooting

### `Codex CLI was not found`

Run:

```powershell
codex --version
```

If that fails, install Codex or add its install directory to `PATH`. On Windows, the script also checks:

```text
%LOCALAPPDATA%\Programs\OpenAI\Codex\bin\codex.exe
```

### Codex is installed but the pipeline fails

Run:

```powershell
codex doctor
codex login
```

Then retry:

```powershell
python agentic_resume.py
```

Check the step log under:

```text
outputs/agentic/<run-name>/logs/
```

### `job_description.txt` is empty

Paste the full job description into `job_description.txt`, save it, and rerun:

```powershell
python agentic_resume.py
```

### Git push says `src refspec main does not match any`

That means the local branch is not named `main` yet, or no commit exists. After committing, run:

```powershell
git branch -M main
git push -u origin main
```

### LaTeX compile errors

The main workflow only generates `.tex`. PDF generation requires a local LaTeX install. If `pdflatex` is missing, install MiKTeX or TeX Live and restart the terminal.

## Suggested First-Time Checklist

```powershell
git clone https://github.com/zake1416/resapp.git
cd resapp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
codex login
codex doctor
notepad job_description.txt
python agentic_resume.py
```

