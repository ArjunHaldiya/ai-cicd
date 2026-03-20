import os
import json
from agents.mistral_client import call_mistral
def review(code: str) -> dict:  
    prompt = f"""
        You are a security code reviewer. Review the following Python code for:
        - Hardcoded secrets (API keys, passwords)
        - SQL injection vulnerabilities
        - Unsafe imports or libraries
        - Missing input validation

        Respond ONLY with valid JSON in this exact format:
        {{
            "passed": true,
            "reason": "No vulnerabilities found",
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
    print(f"Cleaned text: {text}")
    return json.loads(text)