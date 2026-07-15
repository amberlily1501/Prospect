# ADR-0001: LLM Provider Selection

**Status:** Draft

**Date:** July 2026


# 1. Context

Prospect is an AI-powered backend application that researches potential business leads using publicly available information from the web. It verifies the collected information, generates structured company profiles, calculates an ICP (Ideal Customer Profile) score, and prepares an outreach email draft.

Since almost every major feature of the system depends on a Large Language Model (LLM), selecting an appropriate LLM provider is one of the first architectural decisions for the project. The chosen provider should be able to generate reliable structured outputs, support tool calling, integrate easily with a Python backend, and remain affordable because the application may make multiple LLM calls while processing a single lead.

This ADR compares the shortlisted providers and documents the reasoning behind selecting the most suitable one for the initial implementation of Prospect.

# 2. Project Requirements

The selected LLM provider should satisfy the following requirements:

- Support structured JSON outputs.
- Support tool/function calling.
- Provide an official Python SDK.
- Have clear and predictable pricing.
- Be suitable for repeated inference during lead enrichment.
- Support reliable reasoning for verification tasks.
- Integrate easily with FastAPI applications.
- Be actively maintained and well documented.

# 3. Evaluation Criteria

| Evaluation Criteria         | Why it matters for Prospect                                   |
|-----------------------------|---------------------------------------------------------------|
| Structured Outputs          | Required to return valid JSON objects.                        |
| Tool Calling                | Needed for searching, retrieving, and verifying information.  |
| Python SDK                  | Simplifies integration with the FastAPI backend.              |
| Documentation               | Makes development and debugging easier.                       |
| Pricing                     | Reduces operational cost during repeated lead enrichment.     |
| Context Window              | Allows processing information from multiple sources at once.  |
| Reliability                 | Ensures stable API behavior in production.                    |
| Ease of Integration         | Reduces implementation complexity.                            |
| Long-term Maintainability   | Makes future updates easier.                                  |

# 4. Options Considered

The shortlisted options were selected because they satisfy the project's core requirements of supporting structured outputs, tool use, and production-ready APIs (for LLMs), or free/self-hosted search with good coverage (for search strategies). Other providers and services were excluded because they either did not meet the project's requirements, were outside the project scope, or introduced unnecessary cost or complexity.

## Option A — OpenAI
OpenAI was considered because it provides mature APIs, reliable tool calling, structured outputs, and one of the most widely used Python SDKs. Its documentation is comprehensive and integration with FastAPI is straightforward.

The main advantage of OpenAI is its reliability and strong developer ecosystem. However, compared to some competitors, the pricing is moderate rather than the cheapest, which may increase operational costs if the application performs multiple LLM calls during lead enrichment.


## Option B — Anthropic Claude

Anthropic Claude Sonnet 4 was evaluated because it provides strong reasoning capabilities, structured outputs, tool calling, and an official SDK. Claude is well suited for tasks that require careful analysis and long-context reasoning.

Its primary disadvantage for this project is cost. Since Prospect is expected to process many leads, the higher pricing may increase the overall operational budget despite its strong technical capabilities.


## Option C — Google Gemini
Google Gemini 2.5 Flash was considered because it supports structured outputs, tool calling, and provides an official Python SDK. The model offers a very large context window and competitive pricing, making it suitable for applications that repeatedly process large amounts of information.

Gemini's lower cost makes it particularly attractive for Prospect, where multiple LLM calls may be required for each lead. It also integrates well into Python-based backend applications.


# 5. Comparison

| Criteria             | OpenAI GPT-5 mini   |  Claude Sonnet 4 | Gemini 2.5 Flash |  Notes                                   |
|----------------------|---------------------|------------------|------------------|------------------------------------------|
| Structured Outputs   |  Excellent          |  Excellent       |  Excellent       |  All satisfy project requirements.       |
| Tool Calling         |  Yes                |  Yes             |  Yes             |  Required for backend tools.             |
| JSON Schema Support  |  Yes                |  Yes             |  Yes             |  Supported by JSON schema.               |
| Official Python SDK  |  Yes                |  Yes             |  Yes             |  All provide python SDKs.                |
| Documentation        | Excellent           | Excellent        | Very Good        |  All are well documented.                |
| Context Window       | Large               | Very Large       | Very Large       |  Useful for processing long documents.   |
| Pricing              | Moderate            | High             | Low              |  Gemini is the most cost effective.      |
| Integration          | Easy                | Easy             | Easy             |  All integrate well with python/FastAPI. |


# 6. Decision

After evaluating the shortlisted providers against the project's technical and operational requirements, Google Gemini 2.5 Flash is selected as the preferred LLM provider for the initial implementation of Prospect.

All three providers satisfy the project's core functional requirements, including structured outputs, tool calling, official Python SDKs, and reliable APIs. However, Prospect is expected to perform multiple LLM requests for every lead, making cost an important architectural consideration alongside technical capability.

Gemini 2.5 Flash provides the required features while offering the most cost-effective pricing among the evaluated options. Its large context window also makes it well suited for processing information collected from multiple web sources during lead enrichment.

For these reasons, Gemini 2.5 Flash is selected for the first version of the system. This decision can be revisited in the future if project requirements or pricing models change.

# 7. Consequences

## Positive Consequences

- Lower operational cost during development and testing.
- Supports structured outputs required by the backend.
- Official Python SDK simplifies implementation.
- Large context window allows processing information from multiple sources.

## Negative Consequences

- The project becomes dependent on Google's API availability.
- Future pricing or rate-limit changes may affect operational costs.
- If future requirements demand stronger reasoning, a different model may be reconsidered.

# 8. Budget Estimate

Estimated LLM calls per enriched lead:

- Company research
- Fact verification
- ICP scoring
- Email generation

Estimated calls per lead: 4–6

Expected development testing:
Approximately 200–300 enrichments.

Based on current pricing, the expected development cost is only a few US dollars. A budget of USD 10 is expected to be sufficient for development and evaluation.

# 9. Approval Request

I request approval to use Google Gemini 2.5 Flash as the primary LLM provider for the Prospect project.

The selected provider satisfies the functional requirements defined in the SRS while minimizing operational costs. An initial API budget of USD 10 is requested to support development, testing, and evaluation.

If future project requirements change, this decision can be reviewed and another provider can be adopted if necessary.

# References

- Google AI for Developers Documentation
- Google Gemini API Pricing
- OpenAI API Documentation
- OpenAI API Pricing
- Anthropic API Documentation
- Anthropic API Pricing
