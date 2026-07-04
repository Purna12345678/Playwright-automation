from agents.website_agent import WebsiteExplorerAgent


url = input("Website URL : ")

agent = WebsiteExplorerAgent()

result = agent.explore(url)

print(result)