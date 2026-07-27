BLOCKED_PHRASES = [
    "ignore previous instructions",
    "ignore all previous instructions",
    "forget previous instructions",
    "system prompt",
    "developer message",
    "reveal your prompt",
    "act as",
    "pretend to be",
    "jailbreak",
    "you are chatgpt",
    "ignore the rules"
]


def clean_page(text: str) -> str:
    """
    Remove common prompt injection attempts from retrieved webpages.
    """

    lower_text = text.lower()

    for phrase in BLOCKED_PHRASES:
        if phrase in lower_text:
            lower_text = lower_text.replace(phrase, "[REMOVED]")

    return lower_text