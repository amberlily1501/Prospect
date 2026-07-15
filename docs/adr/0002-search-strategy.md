# ADR-0002: Search Strategy

**Status:** Draft

**Date:** July 2026

---

# 1. Context

Prospect gathers publicly available information about potential business leads before generating structured outputs and outreach content. Since the quality of the generated results depends heavily on the quality of the retrieved information, selecting an appropriate search strategy is an important architectural decision.

The search solution should provide reliable access to publicly available web content while remaining cost-effective. According to the project requirements, the system should avoid paid search APIs where possible, meaning the search strategy should rely on free or self-hosted technologies without sacrificing the quality of retrieved information.

This ADR evaluates different search strategies and selects the one that best balances cost, reliability, flexibility, and implementation complexity.

# 2. Project Requirements

The selected search strategy should:

- Use free or self-hosted services where possible.
- Retrieve information from publicly available sources.
- Produce relevant search results for company research.
- Support integration with the Python backend.
- Be reliable enough for repeated automated searches.
- Minimize operational costs.
- Allow future improvements without major architectural changes.

# 3. Evaluation Criteria

| Evaluation Criteria |   Why it matters for Prospect                            |
|---------------------|----------------------------------------------------------|
| Cost                | The SRS requires minimizing non-LLM expenses.            |
| Search Quality      | Better search results improve lead enrichment.           |
| Reliability         | The service should be stable for repeated use.           |
| Ease of Integration | Should integrate easily into the Python backend.         |
| Scalability         | Should support future growth.                            |
| Maintainability     | Should remain easy to update or replace.                 |
| Coverage            | Should retrieve results from a wide variety of websites. |

# 4. Options Considered

## Option A — DuckDuckGo Search

DuckDuckGo was considered because it provides free web search without requiring a paid subscription. It is simple to use and can retrieve publicly available information from a wide range of websites.

The main advantage of DuckDuckGo is its simplicity and zero direct cost. However, it provides limited control over search behavior and may not always return consistent results for automated backend applications. It is also not designed specifically as a backend search service.


## Option B — Self-hosted SearXNG

SearXNG was evaluated because it is an open-source metasearch engine that aggregates results from multiple search engines. It can be self-hosted, giving the project complete control over configuration and avoiding dependence on a single commercial search provider.

Its main strengths are flexibility, privacy, and the ability to customize search behavior. However, it requires additional setup and maintenance since the development team is responsible for hosting and managing the service.


## Option C — Hybrid Search Strategy

The hybrid strategy combines SearXNG for discovering relevant web pages with direct fetching of selected pages and structured information from sources such as Wikipedia and Wikidata when available.

This approach provides broader coverage than relying on a single search provider while keeping operational costs low. It also allows the system to verify information using multiple independent sources before passing it to the LLM for analysis. Although this strategy is slightly more complex to implement, it offers better flexibility and supports future improvements without major architectural changes.


# 5. Comparison

| Criteria            | DuckDuckGo | Self-hosted SearXNG | Hybrid Strategy |
|---------------------|------------|---------------------|-----------------|
| Cost                | Low        | Low                 | Low             |
| Search Quality      | Good       | Very Good           | Excellent       |
| Reliability         | Good       | Very Good           | Excellent       |
| Coverage            | Good       | Excellent           | Excellent       |
| Ease of Integration | Easy       | Moderate            | Moderate        |
| Flexibility         | Limited    | High                | Very High       |
| Scalability         | Moderate   | High                | High            |
| Maintainability     | Easy       | Moderate            | Moderate        |


# 6. Decision

After evaluating the available options, the Hybrid Search Strategy is selected for the Prospect project.

Although DuckDuckGo provides a simple and free solution, it offers limited control over automated searches. SearXNG provides greater flexibility through self-hosting and aggregation of multiple search engines, but relying only on SearXNG may still limit access to structured information.

The hybrid strategy combines the strengths of multiple approaches. SearXNG is used to discover relevant web pages, direct page fetching retrieves the required content, and trusted structured sources such as Wikipedia or Wikidata can be used when appropriate.

This approach provides better search coverage, improves information verification, and keeps operational costs low while remaining flexible for future enhancements.


# 7. Consequences

## Positive Consequences

- No dependency on paid search APIs.
- Better coverage by combining multiple information sources.
- Easier verification using independent sources.
- Flexible architecture that can evolve over time.

## Negative Consequences

- More components need to be maintained.
- Initial implementation is more complex than using a single search provider.
- Search quality still depends on publicly available web content.

# 8. Implementation Notes

The proposed implementation follows these steps:

1. Receive the lead information.
2. Search for relevant pages using SearXNG.
3. Retrieve the selected web pages.
4. Extract the textual content.
5. Use Wikipedia or Wikidata when structured information is available.
6. Pass the collected information to the LLM for verification and structured output generation.

This design separates information retrieval from AI reasoning, making the architecture easier to maintain and modify in the future.

# References

- SearXNG Documentation
- DuckDuckGo
- Wikipedia API Documentation
- Wikidata Documentation