import os
import json
from agents.mistral_client import call_mistral

def performance(code: str) -> dict:
    prompt = f"""
        You are a performance code reviewer. Review the following Python code for:
        - Unnecessary or nested loops
        - Inefficient data structures
        - Redundant computations
        - Memory inefficiency

        Respond ONLY with valid JSON in this exact format:
        {{
            "passed": true,
            "reason": "No performance issues found",
            "issues": []
        }}

        If issues are found, set passed to false and list each issue.
        Be concise. Your entire response must be under 200 words.
        Respond ONLY with valid JSON. No text outside the JSON.

        Code to review:
        {code}
    """
    response = call_mistral(prompt)
    text = response.strip().strip("```json").strip("```").strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {
        "passed": False,
        "reason": "Agent response parse error",
        "issues": ["Could not parse reviewer response"]
        }