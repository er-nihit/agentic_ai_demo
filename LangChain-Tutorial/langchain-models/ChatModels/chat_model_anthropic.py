# Get API Key from console.anthropic.com

from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

## WARNING: EACH CODE RUN COSTS ANTHROPIC API CREDITS
## WARNING: EACH CODE RUN COSTS ANTHROPIC API CREDITS
## WARNING: EACH CODE RUN COSTS ANTHROPIC API CREDITS
## WARNING: EACH CODE RUN COSTS ANTHROPIC API CREDITS
## WARNING: EACH CODE RUN COSTS ANTHROPIC API CREDITS


model = ChatAnthropic(model='claude-3.5-sonnet-20241022')

model.invoke("What is the capital of India")