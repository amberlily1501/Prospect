from fastapi import APIRouter
from app.agents.research_agent import research_company

router = APIRouter()


@router.post("/enrich")
def enrich_company(company: dict):

    company_name = company.get("company")

    result = research_company(company_name)

    return result