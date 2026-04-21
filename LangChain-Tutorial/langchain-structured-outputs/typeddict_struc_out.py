from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

# Schema: Simple Dict - Here the AI automatically understand what that key means and generated the output according to each key.

class SimpleReview(TypedDict):
    summary: str
    sentiment: str

# Schema: Annotated - Here we can give a short summary to the AI what each key actually means
# Optional --> Where the particulaar output is optional
class AnnotatedReview(TypedDict):
    key_themes: Annotated[str, "Write down all the key themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "Return sentiment of the review, either positive. negative or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
                         

# The structured output is generated using with_structured_output() function. 
# We can pass the TypedDict class according to the output we want - Annonatedreview or SimpleReview
structured_model = model.with_structured_output(AnnotatedReview)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too maany pre-installed apps that I can't remove. Also, the UI looks outdated compared  to other brabds. Hoping for a softeware update to fix this.""")

print(result)
