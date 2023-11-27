from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv() # take environment vzriable from .env

import streamlit as st
import os

# funcation to load openai model and get respones
def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv('OPEN_API_KEY'),model_name='text-davinci-003',temperature=0.6)
    response = llm(question)
    return response


st.set_page_config(page_title="Thomas Q&A")
st.header("Langchain Application")

input_ = st.text_input("Input: ",key="input")
response = get_openai_response(input_)

submit= st.button("Ask the Question")

if submit:
    st.subheader("The Response is")
    st.write(response)