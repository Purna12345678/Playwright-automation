import json

from agents.gemini_agent import GeminiAgent
from utils.llm_utils import clean_json

ai = GeminiAgent()

response = ai.extract_requirements("""

Login Module

The user should enter username.

The user should enter password.

The Login button authenticates the user.

Display an error for invalid credentials.

""")

data = clean_json(response)

with open(
    "artifacts/requirements.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(data, f, indent=4)

print("Requirements saved.")