from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# We cannot provide any predefined schema using jsonoutputparser (like we do in sturctured outputs). Output is decided by the LLM.
# Here the json parser is called before creating the template since we need to get the output format instructions before passing the request to LLM
parser = JsonOutputParser()


template = PromptTemplate(
    template="Give the name, age and city of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
    # Expected value from get_format_instruction of JsonOutputParser: "Return a JSON object".
)

'''
prompt = template.format() # template.format() works the same template.invoke() for PromptTemplate
print(prompt)

result = model.invoke(prompt)

final_result = parser.parse(result.content) # This is get the output in a JSON object format.
print(final_result)
'''

# Alternative way using chains
chain = template | model | parser
result = chain.invoke({}) # We need o pass an empty dit is there is no input variable otherwise a runtime error will pop up
print(result)