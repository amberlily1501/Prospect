import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agents.research_agent import research_company

with open("evaluation/golden_dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

correct = 0
total = len(dataset)

for sample in dataset:

    print("=" * 60)
    print("Testing:", sample["company"])

    result = research_company(sample["company"])

    if isinstance(result, str):
        predicted = ""
    else:
        predicted = result.get("company_name") or ""

    expected = sample["expected"] or ""

    print("Expected:", expected)
    print("Predicted:", predicted)

    predicted = predicted.lower()
    expected = expected.lower()

    for word in [
        "corporation",
        "corp.",
        "corp",
        "inc.",
        "inc",
        "llc",
        "ltd",
    ]:
        predicted = predicted.replace(word, "")
        expected = expected.replace(word, "")

    predicted = predicted.strip()
    expected = expected.strip()

    if predicted == expected:
        correct += 1

accuracy = correct / total * 100

print("=" * 60)
print("Accuracy:", accuracy, "%")