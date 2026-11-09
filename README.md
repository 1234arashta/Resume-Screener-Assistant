# Resume Screener Assistant

A Streamlit application for evidence-based resume/JD comparison. It generates a structured match report and stores analyses in SQLite.

## Features
- Job description and resume text inputs
- LLM report: 0–100 match score, exactly 5 matching skills, 3 gaps, 3 interview questions
- Pydantic schema validation and one retry
- SQLite persistence and searchable/filterable history
- Empty-input checks, input truncation, API error messages
- Prompt-injection-resistant framing and human-review disclaimer

## Setup
1. Install Python 3.10+ and Git.
2. Create/activate a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\\Scripts\\activate`
   - macOS/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env`; add your OpenAI API key. Never commit `.env`.
5. Run: `streamlit run app.py`

## Architecture
- `app.py`: Streamlit UI, orchestration, API call, validation, persistence and history.
- OpenAI chat completion with JSON response mode.
- Pydantic validates score bounds and exact list lengths.
- SQLite table `analyses` stores candidate label, timestamp, source text and report JSON.

## Design decisions / assumptions
- Resume and JD are pasted as text; PDF/DOCX parsing is outside this first version.
- Input is capped at 20,000 characters per field to control latency/cost.
- The match score is a decision-support estimate, not an objective hiring verdict.
- No protected traits are evaluated; HR must review evidence and make decisions.
- Local SQLite is suitable for a demo; production needs access controls, encryption, retention policies and secure hosting.

## Privacy
Keep API keys in environment variables/secrets. Do not print keys or raw resumes in logs. In production, minimize stored personal data, encrypt at rest/in transit, restrict HR access, define retention/deletion schedules, obtain appropriate notice/consent, and audit access. This demo stores resume/JD text locally in SQLite; delete the database when no longer needed.

## Tests
Run `pytest -q` (see `test_app.py`).
