from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import Optional, Literal
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# Pydantic forces the output from LLM in the required format, which is not a compulsion in the TypedDict

# Output Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write dowwn all the key themes discussed in the review in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment of the review, either positive. negative or neutral")
    pros: Optional[list[str]] = Field(description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(description="Write down all the cons inside a list")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too maany pre-installed apps that I can't remove. Also, the UI looks outdated compared  to other brabds. Hoping for a softeware update to fix this.""")

                         
print(result)