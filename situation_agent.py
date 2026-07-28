from dotenv import load_dotenv

from config import fast_llm


load_dotenv()


def situation_agent(question):

    prompt = f"""
You are a Disaster Situation Analysis Agent.

Your task:
Analyze the user's message and identify the current disaster situation.

Return ONLY:

Hazard:
Risk Level:
Immediate Situation:

Question:
{question}
"""

    # Use FAST_MODEL (llama-3.1-8b-instant)
    response = fast_llm.invoke(prompt)

    return response.content