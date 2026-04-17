from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Task: In this task we will ask LLM for a joke on input topic and then ask LLM again to explain the joke

prompt1 = PromptTemplate(
    template='Tell me a joke on {topic}',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Explain me this joke. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, prompt2, model, parser)

# Here the result will only provide output of the final result, which means it will only print the explanation not the joke.4
# To print joke as well RunnablePassthrough and RunnableParallel can be used. Check runnable_passthough.py
result = chain.invoke({'politics'})

print(result)