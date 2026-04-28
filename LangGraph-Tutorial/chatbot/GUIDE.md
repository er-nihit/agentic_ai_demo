#### PHASE 1: CREATING BACKEND AND FRONTEND

#### PHASE 2: ADD STREAMING OUTPUT IN CHATBOT

#### PHASE 3: ADD DYNAMIC THREADS IN CHATBOT
We will implement threading mechanism in the chatbot to have different chats on different topics in a single go. Each thread will have it's own memory.  

**IMPLEMENTATION PLAN**

1. Add Sidebar  
    - Add sidebar and *New Chat* button  
    - Generate dynamic thread IDs automatically in a new chat.  
    - Display thread_id for each chat in sidebar.  

2. Implement *New Chat* Button  
    - When user clicks on *New Chat* it will automatically create a new chat window with separate memory and new thread_id.  
    - Save the old session  
    - Reset Message history in display screen  

3. Chat History  
    - Create a chat history to store previous conversation from earlier threads.  
    - Display all thread_id in sidebar  as clickable buttons

4. Load Old Thread  
    When sidebar thread_id is clicked, it should restore the messages


#### PHASE 4: CONNECT DATABASE WITH CHATBOT FOR PERMANENT MEMORY

1. Create new frontend and backend files
2. Install Checkpoint-SQLite
3. Implement Database in backend
4. Chat in multiple threads
5. Install and Visualize
6. Integrate to frontend