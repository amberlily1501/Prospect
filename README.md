<<<<<<< HEAD
# Prospect

Prospect is an AI-powered backend application designed to research and enrich potential business leads using publicly available web information.

## Deliverable 0

This repository currently contains the Architecture Decision Records (ADRs) for the initial design decisions.

### ADRs

- ADR-0001 — LLM Provider Selection
- ADR-0002 — Search Strategy

### Repository Structure

```
docs/
└── adr/
    ├── 0001-llm-provider.md
    └── 0002-search-strategy.md

research/
├── llm-notes.md
└── search-notes.md
```

Prepared as part of the Rapide Technologies AI Internship.
=======
Prospect

AI-powered lead research agent.

Features

- Search companies
- Fetch webpages
- Clean webpages
- Research with Gemini
- Verify information
- Calculate ICP
- Generate outreach email
- FastAPI API

Project Structure

app/
    agents/
    services/
    tools/
    api/
    core/

How to run

pip install -r requirements.txt

uvicorn app.main:app --reload

API

POST /research

{
    "company":"Microsoft"
}
>>>>>>> bab7027 (Complete Prospect AI Lead Research Agent)
