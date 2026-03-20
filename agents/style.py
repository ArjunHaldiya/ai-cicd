import os
import json
from agents.mistral_client import call_mistral

def style(code: str) -> dict:
    prompt ="""
            You are a style code reviewer.
            IMPORTANT: Respond ONLY with a JSON object. No markdown, no explanation, no text outside JSON.

            Review this Python code for:
            - Proper naming conventions
            - Missing docstrings
            - Code formatting issues
            - Proper use of comments


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