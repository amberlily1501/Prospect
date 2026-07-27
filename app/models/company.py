from pydantic import BaseModel


class Source(BaseModel):
    url: str
    snippet: str


class CompanyProfile(BaseModel):
    company_name: str
    industry: str
    location: str
    summary: str
    services: list[str]
    sources: list[Source]