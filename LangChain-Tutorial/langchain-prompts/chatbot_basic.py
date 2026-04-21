from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# NOTE: THIS CODE USED A LOT OF OPENAI CREDITS
# NOTE: LONGER THE CODE RUNS, MORE IS THE CREDITS UTILIZED

load_dotenv()
model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You: ") 
    chat_history.append(user_input) # Add user input in chat history
    if user_input == 'exit':
        break
    result = model.invoke(chat_history) # Passing user input to model
    chat_history.append(result.content) # Add AI output in chat history
    print("AI: ",result.content) # Printing the user output provided by AI

print (chat_history)




