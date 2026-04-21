from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

template = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

# This chain will just perform the sentiment analysis
classifier_chain = template | model | parser2

# LLM response for positive feedback
prompt_pos = PromptTemplate(
    template='Write and appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# LLM response for negative feedback
prompt_neg = PromptTemplate(
    template='Write an appropriate response for this negative feedback n {feedback}',
    input_variables=['feedback']
)

# Conditioning is done in chains using RunnableBranch, and works like switch case
# Syntax: RunnableBranch(tuple of condition and chain ending with a default chain)
# branch_chain = RunnableBranch(
#    (condition-1, chain-1),
#    (condition-2, chain-2),
#    default chain --> It is also mandatory
#)
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt_pos | model | parser),
    (lambda x:x.sentiment == 'negative', prompt_neg | model | parser),
    RunnableLambda(lambda x:"Couldn't find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a terrible smartphone'})
print(result)

chain.get_graph().print_ascii()
