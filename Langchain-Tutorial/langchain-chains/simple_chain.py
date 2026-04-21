from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Sample Project: Get a topic from user and generate 5 facts about that topic
template = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

print(result)

# Visualize the chain
chain.get_graph().print_ascii()
