from agents.website_agent import WebsiteExplorerAgent
from agents.brd_agent import BRDAgent
from agents.gemini_agent import GeminiAgent
from utils.llm_utils import clean_json

def website_node(state):

    explorer = WebsiteExplorerAgent()

    website = explorer.explore(state["url"])

    state["website"] = website

    return state



def brd_node(state):

    parser = BRDAgent()

    text = parser.extract(state["brd_path"])

    state["brd_text"] = text

    return state


def requirement_node(state):

    ai = GeminiAgent()

    response = ai.extract_requirements(
        state["brd_text"]
    )

    state["requirements"] = clean_json(response)

    return state