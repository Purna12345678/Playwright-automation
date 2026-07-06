import json

from agents.gemini_agent import GeminiAgent
from utils.llm_utils import clean_json


class MappingAgent:

    def __init__(self):

        self.ai = GeminiAgent()

    def map(self):

        with open(
            "artifacts/website.json",
            encoding="utf8"
        ) as f:

            website = json.load(f)

        with open(
            "artifacts/requirements.json",
            encoding="utf8"
        ) as f:

            requirements = json.load(f)

        prompt = f"""
You are a Senior QA Automation Architect.

You have:

1. Website structure

2. BRD requirements

Your job is to match every requirement
with the corresponding website element.

Generate JSON only.

Website

{json.dumps(website,indent=2)}

Requirements

{json.dumps(requirements,indent=2)}

Output

{{
 "module":
 {{
     "requirement":
     {{
        "exists": true,
        "locator":""
     }}
 }}
}}
"""

        response = self.ai.ask(prompt)

        return clean_json(response)