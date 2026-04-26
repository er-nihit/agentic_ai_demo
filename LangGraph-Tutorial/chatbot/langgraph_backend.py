#### THIS IS BACKEND FILE
#### FRONTEND FILE: streamlut_frontend.py

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import os
import certifi


os.environ['SSL_CERT_FILE'] = certifi.where()
load_dotenv()

# Selecting LLM Model
model = ChatOpenAI(model='gpt-5-nano')

# Creating State class
class ChatbotState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# Creating chat function
def chat(state: ChatbotState):
    messages = state['messages']
    result = model.invoke(messages)
    return {'messages': [result]}

# Creating Graph
graph = StateGraph(ChatbotState)
graph.add_node('chat', chat)
graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

# Enabling Checkpointer
checkpointer = InMemorySaver()

# Creating Workflow
chatbot = graph.compile(checkpointer=checkpointer)


