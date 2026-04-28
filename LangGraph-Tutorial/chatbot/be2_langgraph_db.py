#### THIS IS BACKEND FILE
#### FRONTEND FILES: fe4

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage
from typing import TypedDict, Annotated
from dotenv import load_dotenv
import sqlite3
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

# Connect to db. If db is not present, it will automatically create one
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

# Enabling Checkpointer 
checkpointer = SqliteSaver(conn=conn)

# Creating Workflow
chatbot = graph.compile(checkpointer=checkpointer)

# This lists the history from the thread
# Passing None value means we do not want the data from a specific thread
# rather extract all the threads from the db
# checkpointer.list() provides a generator object which has all the threads
# Executing the loop provides details from a single element of the generator
def retrieve_all_threads():
    all_threads = set()
    # Thread list is passed in the set to avoid repeatation of occurances
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)



#### =====x====x====x====x====x=====x===x====x=====x====x=====x====x=====x====x=====x===

### __D__E__B__u__G____Z__O__N__E__
