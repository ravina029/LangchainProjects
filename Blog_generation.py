import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransfomers


##function to generate the text from LLama 2 
def get_LLama_Response(input_text,no_words,blog_style):
    ## calling our LLAma model
    llm=CTransfomers(model=,
                     model_type='llama',
                     config={'max_new_tokens':256,
                             'temperature':0.01})
    
    ##Prompt Template 
    template="write a blog for {blog_style} profile for a topic {input_text} within {no_words} of words"

    prompt=PromptTemplate(input_variables=["style","text","n_words"],
                          template=template)
    
    #generate response from llama
    response=llm(prompt.format(style=blog_style,text=input_text,no_words=no_words))
    print(response)
    return response

#streamlit app
st.set_page_config(page_title="Generate for any suitable purpose",
    page_icon="**",
    layout='centered',
    initial_sidebar_state='collapsed')


st.header("Generate Blogs")
input_text=st.text_input("Enter the topic of the blog")


##creating column for additional fields
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',('Data Scientist, Common People, Mathematicians, Tech Idustry, Travel, Yoga'),index=0)


submit=st.button('Generate Blog')

if submit:
    st.write(get_LLama_Response(input_text,no_words,blog_style))
