import os

import truststore
truststore.inject_into_ssl()

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "gemini-2.5-flash"

    def ask(self, prompt: str):

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text

    def extract_requirements(self, brd_text: str):

        prompt = f"""
You are a Senior QA Automation Engineer.

Read the BRD below.

Extract:

1. Modules
2. Features
3. Functional Requirements
4. Validation Rules
5. Acceptance Criteria

Return ONLY valid JSON.

BRD

{brd_text}
"""

        return self.ask(prompt)