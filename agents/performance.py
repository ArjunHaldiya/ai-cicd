import os
import json
from agents.mistral_client import call_mistral

def performance(code: str) -> dict:
    prompt = f"""
            You are a performance code reviewer.
            IMPORTANT: Respond ONLY with a JSON object. No markdown, no explanation, no text outside JSON.

            Review this Python code for:
            - Unnecessary loops
            - Inefficient data structures  
            - Redundant computations
            - Memory inefficiency

            Your response must be exactly this format:
            {{
                "passed": true,
                "reason": "No performance issues found",
                "issues": []
            }}

            Code:
            {code}
            """
    response = call_mistral(prompt)
    text = response.strip().strip("```json").strip("```").strip()
    print(f"Cleaned text: {text}")
    return json.loads(text)