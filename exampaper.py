import streamlit as st
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain

# Load the API key from the environment variable 
load_dotenv()
openai_api_key = os.environ.get('OPENAI_API_KEY')
llm=OpenAI(temperature=0.8)

def generate_questions(subject):
    """Generates exam questions and exam title for a given subject using prompts."""

    PromptTemplate_name = PromptTemplate(input_variables=['subject'],
                                         template='I want to create questions for {subject} specific to data Science field. Suggest me a title for the exam paper with maximum 5 words.')

    name_chain = LLMChain(llm=llm, prompt=PromptTemplate_name, output_key='title')

    PromptTemplate_items = PromptTemplate(input_variables=['title'],
                                         template='Give me 10 most important questions for {title}. Provide the importance level also.')

    topic_items_chain = LLMChain(llm=llm, prompt=PromptTemplate_items, output_key='questions')

    chain = SequentialChain(chains=[name_chain, topic_items_chain],
                             input_variables=['subject'],
                             output_variables=['title', 'questions'])

    
    response = chain({"subject": subject})
    title = response['title'].strip()  # Strip extra whitespace from title
    questions = response['questions'].split(",")  # Split questions into a list

    return title, questions  # Return only the title and questions

# Streamlit App
st.title("Data Science Questions Generator for the Selected Topic")

subject = st.sidebar.selectbox("Select a Subject", ("Data Science","Statistics",
                                                    "Machine Learning", "Deep Learning", "NLP"))

if subject:
    # Add a button for question generation
    if st.button("Generate Questions"):
        response_title, response_questions = generate_questions(subject)
        st.header(response_title)
        st.write("**Questions**")
        for question in response_questions:
            st.write(question)

