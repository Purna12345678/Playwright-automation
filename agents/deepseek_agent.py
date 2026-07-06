import truststore
truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
from openai import OpenAI


class DeepSeekAgent:

    def __init__(self):

        load_dotenv()

        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )

        self.model = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

    def extract_requirements(self, brd_text):

        prompt = f"""
You are a Senior QA Engineer.

Read the BRD below.

Extract:

- Modules
- Features
- Functional Requirements
- Validation Rules
- Acceptance Criteria

Return ONLY valid JSON.

BRD:

{brd_text}
"""

        try:

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a QA Automation Expert."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0
            )

            return response.choices[0].message.content

        except Exception as e:
            print("DeepSeek Error:")
            print(e)
            raise