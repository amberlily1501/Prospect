from fastapi import APIRouter

from app.schemas.lead import LeadRequest, LeadResponse
from app.services.lead_service import LeadService

router = APIRouter()

service = LeadService()


@router.post("/enrich", response_model=LeadResponse)
def enrich_lead(request: LeadRequest):

    result = service.enrich(
        request.company,
        str(request.website) if request.website else None
    )

    return result