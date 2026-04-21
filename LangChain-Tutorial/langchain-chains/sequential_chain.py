from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Task in this project:
# Get a topic fromthe user --> Generate detailed report --> Summarize the report
template1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summarize the {report} in 5 points",
    input_variables=['report']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser
result = chain.invoke({'topic':'cricket world cup'})
print(result)

# Visualize the chain
chain.get_graph().print_ascii()