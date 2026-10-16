import re
from dotenv import load_dotenv
load_dotenv()
from langsmith import Client
from llm import get_llm
from agent import graph


client = Client()
judge_llm = get_llm("openai/gpt-oss-20b", max_tokens=100)

def target(inputs:dict) -> dict:
    out=graph.invoke({"message": inputs["message"]})
    return {
        "category": out["category"],
        "tools_called": out.get("tools_called", []),
        "reply": out["reply"],
    }


# 1. Routing accuracy (deterministic)
def routing_correct(outputs: dict, reference_outputs: dict) -> bool:
    return outputs["category"] == reference_outputs["category"]

# 2. Tool-use correctness (deterministic)
def tool_correct(outputs: dict, reference_outputs: dict) -> bool:
    expected, called = reference_outputs["tool"], outputs["tools_called"]
    return (expected in called) if expected else (len(called) == 0)

# 3. LLM-as-judge
def helpfulness(inputs: dict, outputs: dict) -> dict:
    prompt = (
        "You are a strict QA reviewer. Rate this support reply from 1 (useless) to 5 (excellent) "
        "for helpfulness, politeness and accuracy.\n"
        f"Customer message: {inputs['message']}\nReply: {outputs['reply']}\n\n"
        "Answer in exactly this format:\nSCORE: <number>\nREASON: <one sentence>"
    )
    text = judge_llm.invoke(prompt).content
    m = re.search(r"SCORE:\s*([1-5])", text)
    return {"key": "helpfulness", "score": int(m.group(1)) / 5 if m else None, "comment": text}

if __name__ == "__main__":
    client.evaluate(
        target,
        data="triage-eval-v1",
        evaluators=[routing_correct, tool_correct, helpfulness],
        experiment_prefix="baseline-qwen7b",
        max_concurrency=1,      # free tier: avoid rate limits
    )
