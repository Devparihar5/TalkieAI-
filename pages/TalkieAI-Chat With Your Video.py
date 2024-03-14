import streamlit as st
from utils.chat import Chatbot
from langchain_community.embeddings import HuggingFaceEmbeddings 
from langchain_community.vectorstores import Chroma
import re
import os

default_persist_directory = r"chatdb"

with open("style.css", "r") as file:
    custom_css = file.read()
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

st.title("TalkieAI 📽️")

def load_db():
    embedding = HuggingFaceEmbeddings()
    vectordb = Chroma(
        persist_directory=default_persist_directory,
        embedding_function=embedding)
    return vectordb

updated_vector = load_db()
chatbot = Chatbot(updated_vector)
# user_query = st.text_input("Type your query here:")

prompt = st.chat_input("Say something")
if prompt:
    # st.write(f"User has sent the following prompt: {prompt}")
    # Process user query here, you can add your chatbot logic
    st.write(f"You: {prompt}")
    # Add response from the chatbot
    response = chatbot.chat(prompt)
    pattern = r"(Helpful Answer:.+?$)"

    match = re.search(pattern, response, re.DOTALL)

    helpful_answer = match.group(1).strip()
    helpful_answer = helpful_answer.replace("Helpful Answer:", "")
    st.write(f"TalkieAI 📽️:{helpful_answer}")
        