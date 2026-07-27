from app.services.llm_service import ask_llm

answer = ask_llm(
    "What is the capital of Pakistan? Reply with one sentence."
)

print(answer)