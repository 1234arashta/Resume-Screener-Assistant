# Resume Screener Assistant

An AI-powered resume screening application built with Streamlit and Google's Gemini API. It evaluates candidate resumes against job descriptions, generates structured recruitment insights, and maintains an analysis history using SQLite.

## Features

- **AI Resume Analysis:** Compare resumes against job descriptions using Gemini.
- **Match Score:** Generate a candidate compatibility score between 0 and 100.
- **Matching Skills:** Identify the top 5 skills matching the job description.
- **Skill Gaps:** Identify the top 3 missing or underdeveloped skills.
- **Interview Questions:** Generate 3 candidate-specific interview questions.
- **Structured Output:** Validate AI-generated responses using Pydantic.
- **Analysis History:** Store and retrieve candidate analyses using SQLite.
- **Search and Filtering:** Search candidate records and filter by match score.
- **Error Handling:** Handle empty inputs, invalid AI responses, and API errors.

## Tech Stack

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- Pydantic
- SQLite
- Pytest

## Project Structure

```text
Resume_Screener_Assistant/
├── app.py
├── requirements.txt
├── test_app.py
├── .env.example
├── .gitignore
├── README.md
└── AI_USAGE.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/1234arashta/Resume-Screener-Assistant.git
cd Resume-Screener-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure Gemini API

Create a `.env` file in the project directory:

```dotenv
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-3.8-flash
DB_PATH=analyses.db
```

Obtain an API key from [Google AI Studio](https://aistudio.google.com/apikey).

Never commit your actual API key.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Testing

Run the test suite:

```bash
python -m pytest -v
```

## Architecture

1. The user enters a job description and candidate resume.
2. The application sends the screening prompt to the Gemini API.
3. Gemini returns structured candidate evaluation results.
4. Pydantic validates the generated response.
5. The application displays the score, matching skills, skill gaps, and interview questions.
6. The analysis is saved to SQLite.
7. The History page retrieves stored analyses and supports search and score filtering.

## Privacy and Security

- API credentials are stored locally in `.env`.
- `.env` is excluded from version control.
- Candidate analyses are stored locally in SQLite.
- Resume content is sent to the configured Gemini API for analysis.

## Demo Recording

The complete project walkthrough is available here:

[Watch Resume Screener Assistant Demo](
https://github.com/1234arashta/Resume-Screener-Assistant/releases/download/v1.0/Screen.Recording.mp4)


## Author

GitHub: [1234arashta](https://github.com/1234arashta)
