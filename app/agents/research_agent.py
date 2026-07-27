import json

from app.services.email import generate_email
from app.tools.search import search_web
from app.tools.fetch import fetch_page
from app.services.llm_service import ask_llm
from app.services.icp_service import calculate_icp
from app.services.verification_service import verify_company
from app.services.security_service import clean_page


def research_company(company_name: str):

    # Step 1: Search
    results = search_web(company_name)

    if not results:
        return {
            "company_name": None,
            "industry": None,
            "location": None,
            "summary": None,
            "services": [],
            "sources": [],
            "icp": {
                "score": 0,
                "reasons": []
            },
            "email": ""
        }

    # Step 2: Filter relevant search results
    filtered_results = []

    keywords = company_name.lower().split()

    for result in results:

        title = (result.get("title") or "").lower()
        snippet = (result.get("snippet") or "").lower()

        if any(keyword in title or keyword in snippet for keyword in keywords):
            filtered_results.append(result)

    # If filtering removes everything, use original results
    if not filtered_results:
        filtered_results = results

    # Step 3: Fetch page contents
    combined_text = ""

    for result in filtered_results[:3]:

        try:
            page = fetch_page(result["url"])
            page = clean_page(page)

            combined_text += f"""

Source:
{result['url']}

Snippet:
{result['snippet']}

Content:
{page}

"""

        except Exception:
            continue

    # If every fetch failed, use snippets instead
    if combined_text.strip() == "":

        for result in filtered_results[:3]:

            combined_text += f"""

Source:
{result['url']}

Snippet:
{result['snippet']}

"""

    # Step 4: Ask Gemini
    prompt = f"""
You are an AI research assistant.

Research ONLY this company:

{company_name}

Ignore companies with similar names.

Return ONLY valid JSON.

{{
    "company_name": "",
    "industry": "",
    "location": "",
    "summary": "",
    "services": [],
    "sources": [
        {{
            "url": "",
            "snippet": ""
        }}
    ]
}}

Rules:

- Never invent facts.
- Use only the provided information.
- If unknown, use null.
- Services must be a list.
- Every fact should be supported by a source.
- Return ONLY JSON.

Information:

{combined_text}
"""

    answer = ask_llm(prompt)

    # Step 5: Parse JSON safely
    try:
        company = json.loads(answer)

    except Exception:

        return {
            "company_name": None,
            "industry": None,
            "location": None,
            "summary": None,
            "services": [],
            "sources": [],
            "icp": {
                "score": 0,
                "reasons": []
            },
            "email": ""
        }

    # Step 6: Verify
    company = verify_company(company)

    # Step 7: ICP Score
    company["icp"] = calculate_icp(company)

    # Step 8: Email
    company["email"] = generate_email(company)

    return company