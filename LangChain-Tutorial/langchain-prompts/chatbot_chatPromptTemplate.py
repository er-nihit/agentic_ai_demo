from langchain_core.prompts import ChatPromptTemplate


# Here are passing tuple with the keys and values.
# The following keys are only allowed - human, user, ai, assistant, system.
# It is used to predefine the primary user and system message like we did using 
## SystemMessage and HumanMessage using langchain_core.messages for static chats
# ChatPromptTemplate is combination of langchain_core.messages and PromptTemplate  

chat_template = ChatPromptTemplate([
    ('system','You are a helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({
    'domain': 'Cricket',
    'topic': 'Dusra'
})

print(prompt)