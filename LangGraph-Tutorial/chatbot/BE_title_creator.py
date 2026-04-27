from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()
load_dotenv()



model = ChatOpenAI(model='gpt-5-nano')




def create_chat_title(message, model=model):
    template = PromptTemplate(
    template=f"You are an AI Chatbot. Use the message mentioned below to select a chat title in 3-4 words for this session \n {message}"
)
    model.invoke(template)





