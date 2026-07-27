# Prospect

Prospect is an AI-powered backend lead research agent developed as part of the Rapide Technologies AI Internship.

It researches a company using live web search, extracts and verifies publicly available information, calculates an Ideal Customer Profile (ICP) score, and generates a personalized outreach email draft.

---

## Features

- Live company web search
- Webpage fetching and text extraction
- AI-powered company research (Gemini)
- Fact verification
- ICP scoring
- Personalized outreach email generation
- REST API built with FastAPI
- Evaluation dataset for testing

---

## Project Structure

```
app/
├── agents/
├── api/
├── core/
├── models/
├── schemas/
├── services/
├── tools/
└── utils/

docs/
└── adr/

evaluation/

research/
```

---

## Technologies Used

- FastAPI
- Google Gemini Flash
- DuckDuckGo Search (DDGS)
- BeautifulSoup4
- Pydantic
- Python

---

## How to Run

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoint

### POST /enrich

Example request:

```json
{
  "company": "Microsoft"
}
```

The API returns:

- Company information
- Industry
- Location
- Summary
- Services
- Supporting sources
- ICP score
- Personalized outreach email

---

## Evaluation

Run:

```bash
python evaluation/run_eval.py
```

The evaluation checks whether the research agent correctly identifies companies from a small benchmark dataset.

---

## Deliverable 0

Architecture Decision Records:

- ADR-0001 – LLM Provider Selection
- ADR-0002 – Search Strategy

---

Developed for the Rapide Technologies AI Internship.
