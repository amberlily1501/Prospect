def verify_company(company: dict) -> dict:
    """
    Removes unsupported or empty information.
    """

    if not company.get("sources"):
        company["summary"] = None
        company["services"] = []

    if company.get("industry") == "":
        company["industry"] = None

    if company.get("location") == "":
        company["location"] = None

    if company.get("summary") == "":
        company["summary"] = None

    return company