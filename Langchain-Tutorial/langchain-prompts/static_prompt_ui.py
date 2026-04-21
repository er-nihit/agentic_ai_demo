import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

st.header("Research Tool")

## WARNING: Each run costs OpenAI Credits
## Execute using: streamlit run static_prompt_ui.py

user_input = st.text_input("Enter your prompt")

if st.button('Click Me'):
    output = model.invoke(user_input)
    st.write(output.content)