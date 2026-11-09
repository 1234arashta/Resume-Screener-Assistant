# AI Usage Report

## 1. AI Tools Used

### ChatGPT
Used as a development assistant for:
- Planning the application architecture and feature requirements.
- Generating and improving Python/Streamlit code.
- Designing the Pydantic schema for structured resume analysis.
- Implementing SQLite persistence and analysis history.
- Debugging errors and improving documentation.
- Preparing test cases and project documentation.

### Google Gemini API
Integrated into the application to:
- Analyze resumes against job descriptions.
- Generate candidate match scores.
- Identify matching skills and skill gaps.
- Generate candidate-specific interview questions.

## 2. Important Prompts Used

### Prompt 1: Application Development
"Build a Resume Screener Assistant using Streamlit and Python. Accept a job description and resume, analyze candidate suitability using an LLM, generate a match score between 0 and 100, identify the top 5 matching skills, top 3 skill gaps, and 3 interview questions. Validate the output using Pydantic and store analyses in SQLite."

### Prompt 2: Structured AI Output
"Create a structured resume analysis prompt that compares a candidate resume against a job description. Return valid JSON containing candidate name, match score, matching skills, skill gaps, and interview questions. Ensure the score is between 0 and 100 and the output follows the expected schema."

### Prompt 3: History and Error Handling
"Implement an analysis history page using SQLite in Streamlit. Include candidate search, match score filtering, persistent analysis records, and appropriate handling for API errors, empty inputs, and invalid AI responses."

## 3. Examples of AI Mistakes and Corrections

### Example 1: Incorrect API Configuration
**Mistake:** The initial implementation used OpenAI API configuration even though the application was intended to use Google Gemini.

**Correction:** Replaced the OpenAI integration with Google's `google-genai` SDK, updated environment variable names, modified dependencies, and configured Gemini model settings.

**Verification:** Successfully analyzed sample resumes using Gemini and confirmed that results were saved in SQLite.

### Example 2: GitHub Secret Exposure
**Mistake:** An actual Gemini API key was accidentally placed in `.env.example`, causing GitHub Secret Scanning to block the push.

**Correction:** Revoked the exposed API key, generated a new API key, replaced the key in the local `.env`, changed `.env.example` to use a placeholder, and corrected the Git commit.

**Verification:** Successfully pushed the corrected repository to GitHub without exposing the replacement API key.

## 4. Testing and Verification

AI-generated code was reviewed, modified where necessary, and tested through:

- Running the application locally using Streamlit.
- Analyzing a strong sample candidate (Alex Johnson).
- Analyzing a weak sample candidate (Jamie Lee).
- Analyzing a new candidate (Priya Sharma) after updating the Gemini API key.
- Confirming candidate analyses appeared in the SQLite-backed History page.
- Verifying that the application successfully connected to Gemini.

The application was tested manually through its user interface, with automated tests also included in `test_app.py`.

## 5. Responsible AI Usage

- AI-generated code was reviewed and tested before use.
- API credentials were kept in local environment variables.
- Candidate resumes are processed through the configured Gemini API.
- AI-generated match scores are intended as screening assistance, not as the sole basis for recruitment decisions.
- Human review should be used for final hiring decisions.