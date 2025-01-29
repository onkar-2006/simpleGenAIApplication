import streamlit as st
from dotenv import load_dotenv
load_dotenv()
groq_api_key="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"

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

template=ChatPromptTemplate.from_messages(
    [
        ("system" ,"u are the expert in the quetion and the answering give the answer of the ask qution properly"),
        ("user" ,"{input}")
    ]
)

model=ChatGroq(api_key=groq_api_key)
output=StrOutputParser()

chain=template|model|output

st.title("Simple GenAI App")
input_=st.text_input("ask anything which is in your mind")

if input_:
    responce=chain.invoke({"input":input_})
    st.write(responce)


    




