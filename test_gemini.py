from agents.gemini_agent import GeminiAgent

agent = GeminiAgent()

response = agent.ask("""
Say hello.

Return JSON.

{
 "message":"Hello"
}
""")

print(response)