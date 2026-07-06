from agents.brd_agent import BRDAgent
from agents.deepseek_agent import DeepSeekAgent

brd = BRDAgent()

text = brd.extract("BRD\OrangeHRM_BRD.pdf")

ai = DeepSeekAgent()

result = ai.extract_requirements(text)

print(result)