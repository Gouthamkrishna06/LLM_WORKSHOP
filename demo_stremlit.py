import os
from langchain_ollama import ChatOllama
import streamlit as st

llm = ChatOllama(model="llama3:8b")

st.title("ASK ANYTHING")
question = st.text_input("What's your question?")


if question:
    response = llm.invoke(question)
    st.write(response)