from google.genai.errors import ServerError
from app.core.gemini import client
from app.utils.logger import log_llm


def ask_llm(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )

        text = response.text

        log_llm(prompt, text)

        return text

    except ServerError:
        return "Gemini server is busy. Please try again in a few moments."