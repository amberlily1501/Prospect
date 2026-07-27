def calculate_icp(profile):
    score = 0

    if "AI" in profile.industry:
        score += 30

    if "automation" in profile.summary.lower():
        score += 20

    if len(profile.services) >= 5:
        score += 20

    return score