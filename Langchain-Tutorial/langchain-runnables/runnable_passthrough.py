from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnablePassthrough, RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Task: In this task we will ask LLM for a joke on input topic and then ask LLM again to explain the joke.
# But here we will print both the joke and its explanation
prompt1 = PromptTemplate(
    template='Tell me a joke on {topic}',
    input_variables=['topic'],
)

prompt2 = PromptTemplate(
    template='Explain me this joke. \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

# Generate joke
get_joke_chain = RunnableSequence(prompt1, model, parser)

# Executing 2 chain parallelly
# PassthoughRunnable will preserve the 'joke'.
# RunnableSequence will process another chain for explanation
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

# Merge the get_joke_chain and parallel_chain so both the parallel chain gets joke as input.
final_chain = RunnableSequence(get_joke_chain,parallel_chain)

# Here the result will only provide output of the final result, which means it will only print the explanation not the joke.4
# To print joke as well RunnablePassthrough and RunnableParallel can be used. Check runnable_passthough.py
result = final_chain.invoke({'politics'})

print(result)