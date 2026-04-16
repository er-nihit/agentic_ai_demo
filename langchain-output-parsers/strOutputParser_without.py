from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
model_openai = ChatOpenAI()

# Working repo ids
# meta-llama/Meta-Llama-3-8B-Instruct -- BEST
# Qwen/Qwen2.5-7B-Instruct
# Qwen/Qwen2.5-Coder-7B-Instruct -- SLOWER
# HuggingFaceH4/zephyr-7b-beta
# deepseek-ai/DeepSeek-R1-Distill-Qwen-7B

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    task="text-generation",
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

prompt1 = template1.invoke({'topic':'black hole'})

result = model_hf.invoke(prompt1)
#result = model_openai.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

output = model_hf.invoke(prompt2)
#output = model_openai.invoke(prompt2)

print(output.content)