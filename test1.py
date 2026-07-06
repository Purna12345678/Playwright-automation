from agents.brd_agent import BRDAgent

agent = BRDAgent()

text = agent.extract("BRD\OrangeHRM_BRD.pdf")

print(text)