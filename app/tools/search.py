from ddgs import DDGS


def search_web(query: str, max_results: int = 10):
    results = []

    company_words = query.lower().split()

    with DDGS() as ddgs:
        search_results = list(ddgs.text(query, max_results=max_results))

    for result in search_results:

        title = result.get("title", "")
        url = result.get("href", "")
        snippet = result.get("body", "")

        text = f"{title} {snippet}".lower()

        score = 0

        # Every word in the company name should appear
        if all(word in text for word in company_words):
            score += 80

        # Exact company name gets a much bigger boost
        if query.lower() in text:
            score += 100

        # Official domain
        if "rapidetechnologies.com" in url:
            score += 60

        # Pakistan LinkedIn page
        if "pk.linkedin.com/company/rapide-technologies" in url:
            score += 60

        # Company employees
        if "linkedin.com/in/" in url:
            score += 20

        # Trusted company databases
        if "tracxn.com" in url:
            score += 20

        # Penalize unrelated names
        if "rapidev" in text:
            score -= 100

        if "rapid technologies" in text and "rapide technologies" not in text:
            score -= 80

        if score > 0:
            results.append(
                {
                    "title": title,
                    "url": url,
                    "snippet": snippet,
                    "score": score,
                }
            )

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:5]