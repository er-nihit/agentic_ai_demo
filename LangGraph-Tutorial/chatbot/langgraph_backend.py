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

# ====X===X=== EOF : Below code is for testing purpose ===X===X====
## !!!!! Comment all lines below when executing streamlit !!!!!

#CONFIG = {'configurable': {'thread_id': 'thread-1'}}
#initial_state = {'messages':HumanMessage(content='Show me pasta receipe')}

## Normal invoke function
#chatbot.invoke(initial_state, config=CONFIG})

## Using stream function
## 'messages' stream mode is mostly used when streaming is implemented for chatbot
## stream() returns a python generator object
## Loop through the chunks of generator and keep printing unless content becomes empty
#for chunk, metadata in chatbot.stream(
#    initial_state, # State
#    config=CONFIG, # Config
#    stream_mode = 'messages' # Options: updates, values, custom, #messages 
#):
#    ## It keeps printing until it keeps getting the content in chunk
#    if chunk.content:
#        print(chunk.content, end=" ", flush=True)

