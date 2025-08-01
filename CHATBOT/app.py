from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import os
import streamlit as st
import dotenv as env


env.load_dotenv()

# env variable call
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "True"


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful and knowledgeable character named Arjun, a senior software engineer based in India. You work in the IT sector, have strong technical expertise in cloud computing, backend systems, and AI, and often help junior developers. You communicate clearly, use real-world analogies, and sometimes refer to the Indian tech industry and culture in your responses. Keep your answers conversational and concise, like you're talking to a colleague. Avoid long paragraphs."),
        ("user", "Question:{ques}")
    ]
)
# streamlit setup
st.title("Langchain demo with gemma")
user_input = st.text_input("Talk with the Software Dev based in India")

# llm calls
llm = Ollama(model="gemma3:4b")
output_parser = StrOutputParser()

# chain
chain = prompt | llm | output_parser

if user_input:
    st.write(chain.invoke({'ques': user_input}))