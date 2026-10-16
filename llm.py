from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

def get_llm(
    model_id: str = "openai/gpt-oss-20b",
    max_tokens: int = 256,
):
    return ChatGroq(
        model=model_id,
        max_tokens=max_tokens,
        temperature=0.1,
    )
