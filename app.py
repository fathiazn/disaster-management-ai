import streamlit as st
from orchestrator import orchestrator


# Page configuration
st.set_page_config(
    page_title="Disaster Management AI Assistant",
    page_icon="🚨",
    layout="wide"
)


st.title("🚨 Disaster Management AI Assistant")

st.markdown(
    "Ask questions about disaster preparedness, emergency response, or disaster situations."
)


# Sidebar
with st.sidebar:

    st.header("About")

    st.write("""
This AI Assistant uses:

✅ Router Agent

✅ Emergency Agent

✅ Preparedness Agent

✅ Situation Agent

✅ Planner Agent

✅ Reflection Agent

✅ FAISS + PDF Knowledge Base

✅ Groq Multi-Model LLM Architecture

⚡ Fast Model:
Llama 3.1 8B
(for quick disaster responses)

🧠 Reasoning Model:
Llama 3.3 70B
(for planning and quality review)
""")


    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()



# Chat History
if "messages" not in st.session_state:

    st.session_state.messages = []



# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])



# User input
question = st.chat_input(
    "Ask a disaster management question..."
)


if question:


    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )


    with st.chat_message("user"):

        st.markdown(question)



    # Generate assistant response
    with st.chat_message("assistant"):


        with st.spinner("Analyzing your request..."):


            answer = orchestrator(question)


            st.markdown(answer)



    # Store assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )