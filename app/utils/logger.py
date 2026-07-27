import json
from datetime import datetime


def log_llm(prompt, response):

    log = {
        "time": str(datetime.now()),
        "prompt_length": len(prompt),
        "response_length": len(response)
    }

    with open("llm_logs.jsonl", "a", encoding="utf-8") as file:
        file.write(json.dumps(log) + "\n")