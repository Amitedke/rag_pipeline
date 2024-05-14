from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os

from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. please respont to user queries"),
        ("user","Question:{question}")
    ]
)

st.title = ('lanchain demo')
input_text = st.text_input("Search topic you want")

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser


if input_text:
    st.write(chain.invoke({'question':input_text}))