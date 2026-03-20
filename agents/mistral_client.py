import os
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("MISTRAL_API")
)

def call_mistral(prompt: str) -> str:
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="mistralai/mistral-small-latest",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=500
            )
            content = response.choices[0].message.content
            if content is None:
                content = response.choices[0].message.reasoning_content
            return content
        except Exception as e:
            print(f"API Error on attempt {attempt + 1}: {e}")
            print(f"FULL ERROR: {type(e).__name__}: {e}")
            if attempt == max_retries - 1:
                return '{"passed": false, "reason": "API timeout — all retries exhausted", "issues": ["Mistral API unavailable"]}'
            time.sleep(2 ** attempt)

    return '{"passed": "failure", "reason": "Unknown", "issues" : [] }'