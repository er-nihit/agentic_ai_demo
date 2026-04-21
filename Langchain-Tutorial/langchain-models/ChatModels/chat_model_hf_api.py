# Import API Token from Hugging Face Website. Limited free access is present
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# In huggingface, we need to define the repo id of model we are planning to use
# HuggingfaceEndpoint is used to use the model directly using API Key instead to 
# manually downloading the model locally. It has limited access in free tier.
llm = HuggingFaceEndpoint(
    repo_id='meta-llama/Meta-Llama-3-8B-Instruct',
    task='text-generation'
)

## HUGGING FACE ACCESS TKN HAS ONLY AS LIMITED FREE ACCESS ALLOWED, THEN IT'S CHARGABLE
## HUGGING FACE ACCESS TKN HAS ONLY AS LIMITED FREE ACCESS ALLOWED, THEN IT'S CHARGABLE
## HUGGING FACE ACCESS TKN HAS ONLY AS LIMITED FREE ACCESS ALLOWED, THEN IT'S CHARGABLE
## HUGGING FACE ACCESS TKN HAS ONLY AS LIMITED FREE ACCESS ALLOWED, THEN IT'S CHARGABLE
## HUGGING FACE ACCESS TKN HAS ONLY AS LIMITED FREE ACCESS ALLOWED, THEN IT'S CHARGABLE


model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the Capital of India")
print(result)

# This code is currently throwing errors. Need to search for a model which is currently supported using APi call.
