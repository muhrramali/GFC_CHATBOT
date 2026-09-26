import streamlit as st

from simple_financial_chatbot import simple_chatbot

st.set_page_config(page_title="GFC Financial Chatbot", page_icon="💰", layout="centered")

st.title("GFC Financial Chatbot")
st.caption("Microsoft · Tesla · Apple | FY 2023–2025")

prompt_examples = [
    "What is the total revenue?",
    "How has net income changed over the last year?",
    "What is the operating cash flow?",
    "Which company performed best?",
    "Give me key insights",
]

selected = st.selectbox("Choose a sample question", ["-"] + prompt_examples)
user_query = st.text_input("Ask a predefined financial question", value=(selected if selected != "-" else ""))

if st.button("Ask") or user_query:
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        response = simple_chatbot(user_query)
        st.markdown("### Answer")
        st.write(response)
