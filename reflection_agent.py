from dotenv import load_dotenv

from config import reasoning_llm


# Load environment variables
load_dotenv()


def reflection_agent(message):

    print("REFLECTION_AGENT_V2_LOADED")


    # Extract content from structured agent message
    answer = message["content"]


    prompt = f"""
You are a Quality Review AI Agent for a Disaster Management Assistant.

Your task:
Review and improve the answer.

Rules:
- Correct grammar mistakes.
- Improve clarity.
- Keep the answer concise.
- Keep all important safety instructions.
- Keep the Sources section unchanged.
- Do not explain your review.
- Do not write "Review Results".
- Do not write recommendations.
- Return only the improved final answer.

Original Answer:

{answer}

Improved Final Answer:
"""


    # Use REASONING_MODEL (llama-3.3-70b-versatile)
    response = reasoning_llm.invoke(prompt)


    return response.content