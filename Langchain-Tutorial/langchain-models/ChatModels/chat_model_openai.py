from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4')
# optional parameters
# temperature: Lower value lower creativity, Higher valure higher creativity
# More creativity means more different outputs everytime model is executed
# max_completion_token: Number of max token allowed as result

## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS
## WARNING: EACH CODE RUN COSTS OPENAI API CREDITS

result = model.invoke("Generate a poem on AI")
print(result)

# This result will show a lot of parameters as output. 
# To get the exact output, result.content is used.
print(result.content)
