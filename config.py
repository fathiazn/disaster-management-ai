import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq


# Load environment variables
load_dotenv()


# Fast model for quick disaster response tasks
# Used by:
# - Emergency Agent
# - Situation Agent
# - Preparedness Agent
FAST_MODEL = "llama-3.1-8b-instant"


# Strong reasoning model for planning and quality review
# Used by:
# - Planner Agent
# - Reflection Agent
REASONING_MODEL = "llama-3.3-70b-versatile"


# Fast LLM instance
fast_llm = ChatGroq(
    model=FAST_MODEL,
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)


# Reasoning LLM instance
reasoning_llm = ChatGroq(
    model=REASONING_MODEL,
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)