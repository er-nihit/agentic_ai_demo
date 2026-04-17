from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

# Task: Generate a report on {Topic}
# If the length of report is more than 500, pass to LLM again to summarize it
# If the length is less than 500, directly print the report
prompt = PromptTemplate(
    template='Write a detailedreport on {topic}',
    input_variables=['topic']
)

prompt_summarize = PromptTemplate(
    template='Summarize the following \n {text}',
    input_variables=['text']
)

# Generating the report
gen_report_chain = RunnableSequence(prompt, model, parser)

# Invoking condition: Where length is greater than 500
# RunnableBranch((cond1,task1), task2)
parallel = RunnableBranch(
    (lambda x:len(x.split())>100, RunnableSequence(prompt_summarize, model, parser)),
    RunnablePassthrough()
)

final = RunnableSequence(gen_report_chain, parallel)

print(final.invoke({'topic': 'AI'}))

