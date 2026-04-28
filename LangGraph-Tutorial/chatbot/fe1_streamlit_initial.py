### THIS IS FRONTEND FILE
### BACKEND FILE: be1_langgraph.py

import streamlit as st
from be1_langgraph import chatbot
from langchain_core.messages import HumanMessage

# First creating a thread for config
CONFIG = {
    'configurable': {
        'thread_id': 'thread-1'
    }
}

# Creating a Stream Session for storing the convesation history
# Session state is ideally a python list which stored the conversation history
# Each list item is one message block
# Create a dictionary "conversation_histiry" with 2 components:
#   role: Who is speaking - User or Assistant
#   content: What is the content of message

# Example: 
#[{
#    'role': 'user',
#    'content': 'What are you doing'
#},
#{
#    'role': 'assistant',
#    'content': 'I am sleeping'
#}]


# This condition checks, if there is no conversation history, create one
# If it already exists, no action needed
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

for message in st.session_state['conversation']:
    
    # This block creates a single message block in UI
    # st.chat_message() function is used to create a message block
    #   It is used along with 'with', like we aare writing in a file
    # st.text() is used to provide a text content in that block
    # According to the role, st automatically assigns a small DP
    # Here, it just loads the exists conversation in the screen
    with st.chat_message(message['role']):
        st.text(message['content'])

    
# st.chat_input() function creates a input field as chat window
# It is similar to st.input() but with chat UI look.
user_input = st.chat_input('Type here')

# Check whether user provided any input
# After pressing send/Enter, it checks if there was any value in chatbox
# If input is found then perform action
if user_input:

    # Add the user input in message history
    # The conversation is added as dict as defined above
    st.session_state['conversation'].append({
        'role': 'user',
        'content': user_input
    })

    # Here, it adds the new user message into the conversation screen
    # We are defining user since this a user input
    with st.chat_message('user'):
        st.write(user_input)

    # Once the user side message is add in the conversation. Invoke Chatbot
    # We have imported the chaatbot object from backend python file
    # Pass the user_message as defined in the chatbot object
    ## This is using invoke function - Dumps all output at once
    response = chatbot.invoke({'messages':HumanMessage(content=user_input)}, config=CONFIG)


    # Response in recevied metadata and multiple additional information.
    # Filter out only the last message content in the screen
    assistant_message = response['messages'][-1].content

    # Add the assistant output in conversation dict
    # The conversation is added as dict as defined above
    st.session_state['conversation'].append({
        'role': 'assistant',
        'content': assistant_message
    })

    # Similar to user message, we will assistant message in the chat UI
    with st.chat_message('assistant'):
        st.write(assistant_message)