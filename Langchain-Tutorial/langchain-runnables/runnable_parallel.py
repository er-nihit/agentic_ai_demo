from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt1 = PromptTemplate(
    template='Create a twitter post on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Create a LinkedIn post on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

# The output of each sequence is saved in a key. By default all the output of a runnable are in dict format.
# We can use same or different models for both the chains, it ddoesn't matter
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2,model,parser)
})

# Now the result is a dict as it has output from both the chains.
# result['tweet'] will show output from first chain
# result ['linkedin'] will show output from the second chain
result = parallel_chain.invoke({'topic':'AI'})
print (result)