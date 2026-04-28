### THIS IS FRONTEND FILE
### BACKEND FILE: be2


#XXXXXXXXXXXXXXXXXXX REQUIRED IMPORTS XXXXXXXXXXXXXXXXXXXX
# Python Imports
import streamlit as st
from langchain_core.messages import HumanMessage
import uuid
# Personal Imports
from be2_langgraph_db import chatbot, retrieve_all_threads

#XXXXXXXXXXXXXXXXXXXX UTILITY FUNCTIONS XXXXXXXXXXXXXXXXXXXXX

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    st.session_state['thread_list'].append(thread_id)
    st.session_state['conversations'] = []

def add_thread_to_thread_list(thread_id):
    if thread_id not in st.session_state['thread_list']:
        st.session_state['thread_list'].append(thread_id)

def load_conversations(thread_id):
    return chatbot.get_state(config={'configurable':{'thread_id': thread_id}}).values['messages']


#XXXXXXXXXXXXXXXXXXXXXXXXX SESSION SETUP XXXXXXXXXXXXXXXXXXXXXXXX

session_state_dict_structure_sample = {
    'conversations' : [{
        'role': 'user',
        'content': 'My name is Nihit'
    },
    {
        'role': 'assistant',
        'content': 'Hello Nihit, how can I help you?'
    }],
    'thread_id': 'thread-2',
    'thread_list': ['thread-1', 'thread-2', 'thread-3'],
}

if 'conversations' not in st.session_state:
    st.session_state['conversations'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

# Here we are retrieving all the exisitng threads from db
if 'thread_list' not in st.session_state:
    st.session_state['thread_list'] = retrieve_all_threads()

add_thread_to_thread_list(st.session_state['thread_id'])



#XXXXXXXXXXXXXXXXXXXXXXXXXXX SIDEBAR UI XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

st.sidebar.title('Apun ka Chatbot')
if st.sidebar.button('New Chat'):
    reset_chat()
st.sidebar.header('My conversations')

for thread_id in st.session_state['thread_list'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id   

        messages = load_conversations(thread_id)
        
        temp_messages = []
        for message in messages:
            if isinstance(message, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({'role': role, 'content': message.content})

        st.session_state['conversations'] = temp_messages
            


#XXXXXXXXXXXXXXXXXXXXXXXXXX MAIN UI XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

for message in st.session_state['conversations']:
    
    with st.chat_message(message['role']):
        st.text(message['content'])

    
user_input = st.chat_input('Type here')

if user_input:

    st.session_state['conversations'].append({
        'role': 'user',
        'content': user_input
    })

    with st.chat_message('user'):
        st.write(user_input)

    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    with st.chat_message('assistant'):
        assistant_message = st.write_stream(
            chunk.content for chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    st.session_state['conversations'].append({
        'role': 'assistant',
        'content': assistant_message
    })