### THIS IS FRONTEND FILE
### BACKEND FILE: langgraph_backend.py


#XXXXXXXXXXXXXXXXXXX REQUIRED IMPORTS XXXXXXXXXXXXXXXXXXXX
# Python Imports
import streamlit as st
from langchain_core.messages import HumanMessage
import uuid
# Personal Imports
from langgraph_backend import chatbot

#xxxxxxxxxXXXXxxxxxxxxxx UTILITY FUNCTIONS XXXXXXXXXXXXXXXXXXXXX

# P3.1.2 Creating a random thread id for each session
def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

# P3.2 Reset current chat
def reset_chat():
    thread_id = generate_thread_id() # Generate new thread_id
    st.session_state['thread_id'] = thread_id # Assign new thread_id to session
    st.session_state['thread_list'].append(thread_id) # P3.3.1 Add thread_id in list whenever New chat is clicked
    st.session_state['conversations'] = [] # Clear current chat window

# P3.3 Create thread_list for sidebar
def add_thread_to_thread_list(thread_id):
    # First check if the thread_id is not already present in the thread_list
    if thread_id not in st.session_state['thread_list']:
        st.session_state['thread_list'].append(thread_id)

# P3.4 Load conversations when corresponding thread_id is clicked
# Use get_state() function to load all conversations for a particular thread using the thread_id provided
def load_conversations(thread_id):
    # Here we are extracting the values then messages from it, since the metadata is not needed
    return chatbot.get_state(config={'configurable':{'thread_id': thread_id}}).values['messages']



#XXXXXXXXXXXXXXXXXXXXXXXXX SESSION SETUP XXXXXXXXXXXXXXXXXXXXXXXX

# Dict structure for each list element in st.session()
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

# This condition checks, if there is no conversation history, create one
# If it already exists, no action needed
if 'conversations' not in st.session_state:
    st.session_state['conversations'] = []

# P3.1.2 Check and assign thread_id to the session. 
# thread_id is unique for each session
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

# P3.3.1 Create a list of threads for sidebar
# For the initial setup if the thread_list is there, just create a list
# We need to append thread_id to this list only 2 times:
#   - Initial Session
#   - When 'New Chat' button is clicked
if 'thread_list' not in st.session_state:
    st.session_state['thread_list'] = []

# P3.3.1 Run everytime the session is invoked
add_thread_to_thread_list(st.session_state['thread_id'])



#XXXXXXXXXXXXXXXXXXXXXXXXXXX SIDEBAR UI XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# P3.1.1 Adding Sidebar
st.sidebar.title('Apun ka Chatbot')
if st.sidebar.button('New Chat'):
    reset_chat() # P3.2 Reset chat if button is clicked
st.sidebar.header('My conversations')

# P3.1.3 Display current thread_id in sidebar
#st.sidebar.text(st.session_state['thread_id'])

# P3.3.2 Show all thread_ids in sidebar as clickable buttons
for thread_id in st.session_state['thread_list']:
    if st.sidebar.button(str(thread_id)):
        # P3.4 Load the session of the selected thread_id
        st.session_state['thread_id'] = thread_id   

        # P3.4 If the button is clicked, load_conversations() is called
        # It wil return the messages using get_state() of the thread_id
        messages = load_conversations(thread_id)
        
        # These messages will be used to update the state of the session
        # For that we will update the conversations in st.session_state()
        # Iterate through the messages to matchthe format in converation dict
        temp_messages = []
        for message in messages:
            # Check if message is HumanMessage or AIMessage
            if isinstance(message, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            # Now append the role and content for conversations dict
            temp_messages.append({'role': role, 'content': message.content})

        st.session_state['conversations'] = temp_messages
            


#XXXXXXXXXXXXXXXXXXXXXXXXXX MAIN UI XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

for message in st.session_state['conversations']:
    
    # This block creates a single message block in UI
    # st.chat_message() function is used to create a message block
    #   It is used along with 'with', like we aare writing in a file
    # st.text() is used to provide a text content in that block
    # According to the role, st automatically assigns a small DP
    # Here, it just loads the exists conversations in the screen
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
    # The conversations is added as dict as defined above
    st.session_state['conversations'].append({
        'role': 'user',
        'content': user_input
    })

    # Here, it adds the new user message into the conversations screen
    # We are defining user since this a user input
    with st.chat_message('user'):
        st.write(user_input)

    # Config for the chatbot
    # P3.1.2 Adding dynamic thread_id
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    ## STREAM IMPLEMENTATION WITH GENERATOR USING LANGGRAPH
    # st.write_stream() function adds a typewriter effect in outputs
    # We need to pass the generator object to get that effect
    # Streamlit takes care of the UI 
    # We are executing a for loop to get only the content of the stream 
    with st.chat_message('assistant'):
        assistant_message = st.write_stream(
            chunk.content for chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode='messages'
            )
        )

    # Adding the AI message output in history
    st.session_state['conversations'].append({
        'role': 'assistant',
        'content': assistant_message
    })