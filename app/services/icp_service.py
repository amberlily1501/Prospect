def calculate_icp(company: dict) -> dict:
    score = 0
    reasons = []

    industry = str(company.get("industry", "")).lower()
    summary = str(company.get("summary", "")).lower()
    services = company.get("services", [])

    keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "automation",
        "computer vision",
        "nlp",
        "predictive"
    ]

    for keyword in keywords:
        if keyword in industry or keyword in summary:
            score += 15

            reason = f"Works in {keyword}"

            if reason not in reasons:
                reasons.append(reason)

    if len(services) >= 5:
        score += 15

        if "Offers many AI services" not in reasons:
            reasons.append("Offers many AI services")

    location = str(company.get("location", "")).lower()

    if any(country in location for country in [
        "usa",
        "united states",
        "uk",
        "london",
        "germany",
        "berlin",
        "pakistan"
    ]):
        score += 10

        if "Located in target market" not in reasons:
            reasons.append("Located in target market")

    score = min(score, 100)

    return {
        "score": score,
        "reasons": reasons
    }