import os

from dotenv import load_dotenv

from retriever import retriever_agent
from config import fast_llm

load_dotenv()


def emergency_agent(question):

    # Retrieve relevant emergency information
    context, docs = retriever_agent(question)

    prompt = f"""
You are an Emergency Response AI Agent.

Your job is to give immediate emergency advice.

Rules:
- Focus on immediate safety.
- Give step-by-step instructions.
- Use only the provided context.
- If emergency phone numbers are not in the context, tell the user to contact the local emergency services.
- End your answer with a short reminder to stay safe.

Context:
{context}

Question:
{question}

Answer:
"""

    # Use FAST_MODEL (llama-3.1-8b-instant)
    response = fast_llm.invoke(prompt)

    # Add sources
    sources = []

    for doc in docs:
        source = os.path.basename(
            doc.metadata.get("source", "Unknown")
        )
        page = doc.metadata.get("page", "Unknown")

        sources.append(
            f"- {source} (Page {page})"
        )

    # Remove duplicate sources
    unique_sources = list(dict.fromkeys(sources))

    final_answer = (
        response.content
        + "\n\nSources:\n"
        + "\n".join(unique_sources)
    )

    return final_answer