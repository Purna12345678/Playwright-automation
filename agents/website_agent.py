import json

from utils.browser import BrowserManager


class WebsiteExplorerAgent:

    def explore(self, url):

        browser = BrowserManager()

        page = browser.start()

        page.goto(url)

        page.wait_for_load_state("networkidle")

        title = page.title()

        screenshot = "screenshots/home.png"

        page.screenshot(path=screenshot)

        data = {
            "title": title,
            "url": page.url,
            "buttons": [],
            "inputs": [],
            "links": [],
            "dropdowns": [],
            "tables": [],
            "forms": []
        }

        # Buttons

        buttons = page.locator("button").all()

        for button in buttons:

            try:

                data["buttons"].append({
                    "text": button.inner_text(),
                    "visible": button.is_visible()
                })

            except:

                pass

        # Inputs

        inputs = page.locator("input").all()

        for textbox in inputs:

            try:

                data["inputs"].append({
                    "type": textbox.get_attribute("type"),
                    "name": textbox.get_attribute("name"),
                    "placeholder": textbox.get_attribute("placeholder")
                })

            except:

                pass

        # Links

        links = page.locator("a").all()

        for link in links:

            try:

                data["links"].append({
                    "text": link.inner_text(),
                    "href": link.get_attribute("href")
                })

            except:

                pass

        # Forms

        forms = page.locator("form").count()

        data["forms"] = forms

        # Tables

        data["tables"] = page.locator("table").count()

        # Dropdowns

        data["dropdowns"] = page.locator("select").count()

        with open("artifacts/website.json", "w", encoding="utf-8") as f:

            json.dump(data, f, indent=4)

        browser.stop()

        return data