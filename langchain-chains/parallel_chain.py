from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# TASK --> User will input a topic.
# It will be passed to one model (OpenAI) to generate some notes on that topic
# Same topic will be paassed to another model (HF/Llama) to create quiz questions related to that topic
# Merge output fromboth the LLMs aand create a single document as output

model1 = ChatOpenAI()
model2 = ChatHuggingFace(
    llm=HuggingFaceEndpoint(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        task="text-generation"
    )
)

# Prompt to ask LLM-1 to create notes on the topic
template1 = PromptTemplate(
    template='Create a notes for {topic}',
    input_variables=['topic']
)

# Prompt to asak LLM-2 to create quizzes on the topic
template2 = PromptTemplate(
    template='Create 5 short quiz questions and answers on {topic}',
    input=['topic']
)

# Prompt to ask LLM (either LLM) to merge the outputs of previous 2 prompts (notes + quiz)
template3 = PromptTemplate(
    template='Merge the provided  notes and quiz into a document \n Notes -> {notes} \n Quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

# Using RunnableParallel to create 2 chain which can be executed parallelly
# Inputs are provided as dict where the output value of each chain is key'd 'notes' and 'quiz', so it can be provided as input to prompt3 for merging
parallel_chain = RunnableParallel({
    'notes': template1 | model1 | parser,
    'quiz': template2 | model2 | parser
})


merge_chain = template3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({'topic':'LLM'})

print(result)

chain.get_graph().print_ascii()