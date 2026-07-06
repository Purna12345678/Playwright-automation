import os
import pdfplumber


class BRDAgent:

    def extract(self, file_path: str) -> str:

        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"BRD file not found:\n{file_path}"
            )

        text = ""

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text