
import re
from langgraph.graph import StateGraph,START, END
from dotenv import load_dotenv
from typing import TypedDict  ,Literal
from llm import get_llm

from tools import lookup_order,search_faq


load_dotenv()


class State(TypedDict):
    message:str
    category:Literal["billing","technical","general"]
    tools_called:list[str]
    tool_result:str
    reply:str

llm = get_llm()

CATEGORIES = ["billing", "technical", "general"]

def classify(state:State) -> dict :
    prompt=("Classify the customer support message into exactly one category:\n"
        "- billing: payments, refunds, charges, orders, invoices\n"
        "- technical: bugs, crashes, login problems, performance\n"
        "- general: anything else\n\n"
        "Reply with ONLY the category word.\n\n"
        f"Message: {state['message']}"
    )

    raw=llm.invoke(prompt).content.strip().lower()
    category= next((c for c in CATEGORIES if c in raw), "general") 

    return {"category": category, "tools_called": []}

def billing(state:State) -> dict:
    match=re.search(r"\b(\d{4})\b", state["message"])
    result = lookup_order(match.group(1)) if match else "No order id given"
    return {"tool_result": result, "tools_called": state.get("tools_called", []) + ["lookup_order"]}


def technical(state: State) -> dict:
    return {
        "tool_result": search_faq(state["message"]),
        "tools_called": state.get("tools_called", []) + ["search_faq"],
    }

def general(state: State) -> dict:
    return {"tool_result": "", "tools_called": state.get("tools_called", [])}


def respond(state: State) -> dict:
    prompt = (
        "You are a friendly customer support agent. Write a short reply (2-3 sentences).\n"
        f"Customer message: {state['message']}\n"
        f"Info from our systems: {state.get('tool_result') or 'none'}"
    )
    return {"reply": llm.invoke(prompt).content}

def route(state: State) -> str:
    return state["category"]


builder=StateGraph(State)

builder.add_node("classify", classify)

builder.add_node("billing",billing)
builder.add_node("technical",technical)
builder.add_node("general",general)
builder.add_node("respond",respond)
builder.add_node("route",route)


builder.add_edge(START,"classify")
builder.add_conditional_edges("classify",route,["billing","technical","general"])
for n in ["billing","technical","general"]:
    builder.add_edge(n,"respond")
builder.add_edge("respond",END)


graph=builder.compile()


if __name__ == "__main__":
    import langsmith as ls
    with ls.tracing_context(project_name="triage-agent"):
        for msg in ["Where is my order 1001?", "The app keeps crashing", "What are your support hours?"]:
            out = graph.invoke({"message": msg})
            print(f"[{out['category']}] {msg}\n  -> {out['reply']}\n")