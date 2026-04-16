from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Using pydantic we need to define the schema how we want the output along with the required fields
class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=18, description='Age of the person')
    city:str = Field(description='Name of the city the person belongs to')

# Creating a parser by passing the Person class as object
parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

'''
prompt = template.invoke({'place':'Indian'})
print(prompt)

result = model.invoke(prompt)

final_output  = parser.parse(result.content)

print(final_output)
'''

# Alternative methos using chain
chain  = template | model | parser
result = chain.invoke({'place':'Indian'})
print(result)

