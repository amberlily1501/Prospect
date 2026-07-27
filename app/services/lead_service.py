class LeadService:

    def enrich(self, company: str, website: str | None = None):

        return {
            "company": company,
            "status": "success",
            "message": "Lead received successfully."
        }