import json
import os

from utils.browser import BrowserManager


class WebsiteExplorerAgent:

    def __init__(self):
        self.browser = None
        self.page = None

    def explore(self, url):

        self.browser = BrowserManager()
        self.page = self.browser.start()

        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

        os.makedirs("artifacts", exist_ok=True)
        os.makedirs("screenshots", exist_ok=True)

        data = {
            "page": self.capture_page_info(),
            "elements": self.capture_elements(),
            "statistics": self.capture_statistics()
        }

        self.capture_screenshot()
        self.save_dom()

        try:
            self.save_accessibility()
        except Exception:
            print("Accessibility snapshot not supported.")

        self.save_json(data)

        self.browser.stop()

        return data

    # --------------------------------------------------------
    # Page Information
    # --------------------------------------------------------

    def capture_page_info(self):

        viewport = self.page.viewport_size

        return {
            "title": self.page.title(),
            "url": self.page.url,
            "viewport": viewport
            if viewport
            else {
                "width": 1280,
                "height": 720
            }
        }

    # --------------------------------------------------------
    # Capture every important element
    # --------------------------------------------------------

    def capture_elements(self):

        js = """
        () => {

            const result = [];

            const elements = document.querySelectorAll(
                "input,button,select,textarea,a"
            );

            elements.forEach(el=>{

                let locator="";

                if(el.name){

                    locator=`${el.tagName.toLowerCase()}[name="${el.name}"]`;

                }

                else if(el.id){

                    locator=`#${el.id}`;

                }

                else if(el.type){

                    locator=`${el.tagName.toLowerCase()}[type="${el.type}"]`;

                }

                else{

                    locator=el.tagName.toLowerCase();

                }

                result.push({

                    tag:el.tagName.toLowerCase(),

                    type:el.type || "",

                    id:el.id || "",

                    name:el.name || "",

                    class:el.className || "",

                    placeholder:el.placeholder || "",

                    text:el.innerText || "",

                    role:el.getAttribute("role"),

                    href:el.href || "",

                    locator:locator,

                    visible:el.offsetParent!==null,

                    enabled:!el.disabled

                });

            });

            return result;

        }
        """

        return self.page.evaluate(js)

    # --------------------------------------------------------
    # Counts
    # --------------------------------------------------------

    def capture_statistics(self):

        return {

            "buttons": self.page.locator("button").count(),

            "inputs": self.page.locator("input").count(),

            "links": self.page.locator("a").count(),

            "dropdowns": self.page.locator("select").count(),

            "tables": self.page.locator("table").count(),

            "forms": self.page.locator("form").count(),

            "textareas": self.page.locator("textarea").count()

        }

    # --------------------------------------------------------
    # Screenshot
    # --------------------------------------------------------

    def capture_screenshot(self):

        self.page.screenshot(
            path="artifacts/homepage.png",
            full_page=True
        )

    # --------------------------------------------------------
    # Save HTML
    # --------------------------------------------------------

    def save_dom(self):

        html = self.page.content()

        with open(
            "artifacts/dom.html",
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)

    # --------------------------------------------------------
    # Accessibility
    # --------------------------------------------------------

    def save_accessibility(self):

        snapshot = self.page.accessibility.snapshot()

        with open(
            "artifacts/accessibility.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                snapshot,
                f,
                indent=4
            )

    # --------------------------------------------------------
    # Save Website JSON
    # --------------------------------------------------------

    def save_json(self, data):

        with open(
            "artifacts/website.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4
            )