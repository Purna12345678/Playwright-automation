from agents.website_agent import WebsiteExplorerAgent
from utils.json_utils import save_json

url = input("Website URL : ")

agent = WebsiteExplorerAgent()

website = agent.explore(url)

save_json(
    website,
    "artifacts/website.json"
)

print("Website saved.")