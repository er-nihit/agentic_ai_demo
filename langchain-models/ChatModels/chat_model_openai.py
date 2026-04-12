from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')
# optional parameters
# temperature: Lower value lower creativity, Higher valure higher creativity
# max_completion_token: Number of max token allowed as result
#   

## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS

result = model.invoke("What is the capital of India")
print(result)

# This result will show a lot of parameters as output. 
# To get the exact output, result.content is used.
print(result.content)
