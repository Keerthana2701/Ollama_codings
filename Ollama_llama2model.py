#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from dotenv import load_dotenv


# In[2]:


# pip install -r requirements.txt


# In[3]:


from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# #### set the LANGCHAIN_API_KEY and  LANGCHAIN_PROJECT in .env file of same path

# In[4]:


from dotenv import load_dotenv
load_dotenv()


# In[5]:


print("API KEY:", os.getenv("LANGCHAIN_API_KEY"))   
print("PROJECT:", os.getenv("LANGCHAIN_PROJECT"))


# In[6]:


## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain With Llama3 using OLLAMA")
input_text=st.text_input("Enter your question : ")


## Ollama Llama3 model
llm=Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



# In[7]:


### Save the script to .py and execute to use the streamlit. Stramlit doesn't work with jupyter notebook

