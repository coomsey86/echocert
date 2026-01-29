import json
import sys
import time

"""
Deterministic fake LLM.
Input: JSON with { "prompt": "...", "variant": "A|B|C" }
Output changes ONLY based on variant.
"""

def run(prompt, variant):
    base = {
        "response": "The capital of France is Paris.",
        "confidence": "high",
        "length": "short"
    }

    if variant == "B":
        base["confidence"] = "very high"

    if variant == "C":
        base["extra"] = "Paris has been the capital since 508 AD."

    return base


if __name__ == "__main__":
    payload = json.load(sys.stdin)
    result = run(payload["prompt"], payload["variant"])
    print(json.dumps(result, indent=2))
