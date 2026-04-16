from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model_gpt = ChatOpenAI()

llm = HuggingFaceEndpoint(
    model="google/gemma-2-2b-it",
    task="text-generation"
)
model_hf = ChatHuggingFace(llm=llm)

# 1st Prompt: Detailed Report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd Prompt: Summarize
template2 = PromptTemplate(
    template='Write a 5 lines summaary on the following text \n {text}',
    input_variables=['text']
)

# This automtically collect only the string component from LLM which is useful to user
parser = StrOutputParser()

# Creating chain of commands
chain = template1 | model_hf | parser | template2 |  model_hf | parser

result = chain.invoke({'topic':'black hole'})

print(result)