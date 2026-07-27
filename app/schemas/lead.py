from pydantic import BaseModel, HttpUrl


class LeadRequest(BaseModel):
    company: str
    website: HttpUrl | None = None


class LeadResponse(BaseModel):
    company: str
    status: str
    message: str