import json

from agents.mapping_agent import MappingAgent

agent = MappingAgent()

mapping = agent.map()

with open(
    "artifacts/mapping.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(mapping,f,indent=4)

print("Mapping Generated")