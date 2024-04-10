
#Simple Chatbot Project
import langchain
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()  #as soon as we call it, it take environment variables from .env
import os
import streamlit as st
import warnings

## load OpenAI models and get response

def openai_response(input_text):
    llm=OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),temperature=0.6,model_name='gpt-3.5-turbo-instruct')
    response=llm(input_text)
    return response


#creating streamlit app

st.set_page_config(page_title='Chatbot APP')
st.header("This is application of Langchain")

#Capture the input text
input=st.text_input("Ask: ",key='input')
response=openai_response(input)

submit=st.button('Click to see response')

#fuctionality on clicking the button

if submit:
    st.subheader("Response best to my knowledge")
    st.write(response)