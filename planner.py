from dotenv import load_dotenv

from config import reasoning_llm


load_dotenv()


def planner_agent(message):

    question = message["content"]["question"]
    situation = message["content"]["answer"]


    prompt = f"""
You are a Disaster Response Planning Agent.

Your task:
Create a short and practical action plan.

Question:
{question}

Situation:
{situation}

Rules:
- Prioritize human safety.
- Give simple steps.
- Keep the plan short.

Format:

Step 1:
Step 2:
Step 3:
"""


    response = reasoning_llm.invoke(prompt)

    return response.content