import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

CHROME_PATH = os.getenv("BROWSER_PATH")


class BrowserManager:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        if not CHROME_PATH:
            raise Exception(
                "BROWSER_PATH not found. Check your .env file."
            )

        if not os.path.exists(CHROME_PATH):
            raise Exception(
                f"Browser not found at:\n{CHROME_PATH}"
            )

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            executable_path=CHROME_PATH,
            headless=False
        )

        self.page = self.browser.new_page()

        return self.page

    def stop(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()