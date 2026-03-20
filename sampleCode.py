# sample_code.py

GOOD_CODE = """
import os
import hashlib

def calculate_user_hash(user_id: str) -> str:
    \"\"\"
    Calculates a secure hash for a given user ID.
    
    Args:
        user_id: The user's unique identifier
    Returns:
        A secure SHA256 hash string
    \"\"\"
    api_key = os.getenv("API_KEY")
    if not user_id:
        raise ValueError("user_id cannot be empty")
    return hashlib.sha256(user_id.encode()).hexdigest()


def get_unique_users(users: list) -> list:
    \"\"\"Returns unique users efficiently using a set.\"\"\"
    return list(set(users))
"""

BAD_CODE = """
import os
import pickle

API_KEY = "sk-1234567890abcdef"
DB_PASSWORD = "supersecret123"

def get_users(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if data[i] == data[j]:
                    result.append(data[i])
    return result

def query(u):
    import subprocess
    q = "SELECT * FROM users WHERE name = " + u
    subprocess.call(q)
    return q
"""