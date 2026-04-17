from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Task: Generate joke from {topic} provided
# Analyse number of words in the joke using normal python function (NOT LLM)
# Print Joke and total number of words

prompt = PromptTemplate(
    template='Generate a joke on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

gen_joke_chain = RunnableSequence(prompt, model, parser)

def word_count(text):
    return len(text.split())

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'count': RunnableLambda(word_count)
})

final = RunnableSequence(gen_joke_chain, parallel_chain)

print(final.invoke({'topic':'politics'}))