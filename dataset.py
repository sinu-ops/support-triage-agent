from dotenv import load_dotenv
load_dotenv()
from langsmith import Client

load_dotenv()

client=Client()
NAME="triage-eval-v1"


if client.has_dataset(dataset_name=NAME):
    print("dataseet already exists delete it from ui or change the name ")
    raise SystemExit

dataset=client.create_dataset(NAME,description="support triage test cases")


examples = [
    ("Where is my order 1001?", "billing", "lookup_order"),
    ("I was charged twice for order 1003", "billing", "lookup_order"),
    ("I need a refund for order 1002", "billing", "lookup_order"),
    ("My payment failed on order 1003, what now?", "billing", "lookup_order"),
    ("Can you check the status of 1001 please", "billing", "lookup_order"),
    ("Invoice for order 1002 looks wrong", "billing", "lookup_order"),
    ("The app crashes when I open it", "technical", "search_faq"),
    ("I forgot my password", "technical", "search_faq"),
    ("Everything is really slow today", "technical", "search_faq"),
    ("App keeps crashing after the update", "technical", "search_faq"),
    ("cant reset my pasword", "technical", "search_faq"),
    ("Why is the dashboard so slow?", "technical", "search_faq"),
    ("What are your support hours?", "general", None),
    ("Do you have a student discount?", "general", None),
    ("How do I contact your sales team?", "general", None),
    ("Where is your office located?", "general", None),
    ("Do you ship internationally?", "general", None),
    ("Tell me about your company", "general", None),
    # tricky / ambiguous
    ("I was charged but the app crashed during checkout, order 1003", "billing", "lookup_order"),
    ("Hi", "general", None),
    ("Refund??", "billing", "lookup_order"),
    ("My account is locked and I forgot my password", "technical", "search_faq"),
]


client.create_examples(
    dataset_id=dataset.id,
    examples=[
        {"inputs": {"message": m}, "outputs": {"category": c, "tool": t}}
        for m, c, t in examples],
)
print(f"Created {len(examples)} examples in '{NAME}'")