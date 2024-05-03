from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI



def fix_description(desc):

    prompt = """
   Describe the content of the image in Russian, understandable to a person, based on the information provided: 
    
    Caption: If available, specify the main caption for the image along with the confidence level.

    Dance Captions: If available, list the dance captions 

    Tags: List all tags associated with the image

    Objects: If objects are found, list them 

    People: If people are detected
             """
                
                
    chat = ChatOpenAI(temperature=0.1, openai_api_key="openai_api_key")

    messages = [
        SystemMessage(
            prompt
        ),
        HumanMessage(
            desc )
    ]

    return  str(chat.invoke(messages))
    