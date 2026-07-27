from app.services.llm_service import ask_llm


def generate_email(company: dict) -> str:

    prompt = f"""
You are writing a professional cold outreach email.

Company:

{company}

Write a concise email.

Rules:

- Professional tone
- Under 180 words
- Mention the company's business
- Mention why Rapide Technologies could help
- End with a call to action

Return ONLY the email.
"""

    return ask_llm(prompt)