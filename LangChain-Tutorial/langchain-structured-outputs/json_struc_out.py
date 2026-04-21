from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

# JSON Schema
# JSON Schema does not support default values to a key
# JSON Schema does not allow Automatic data type conversion like TypeDict or Pydantic
json_schema = {
    "title": "Review",
    "type": "object",
    "properties":{
        "key_themes":{
            "type": "array",
            "items": {
                "type": "string"
            },
            "description": "Write down all the key themes discussed in the review in a list"
        },
        "summary":{
            "type": "string",
            "description": "A brief summary of the review"
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "Return the sentiment of the review either positive, negative or neutral"
        },
        "pros": {
            "type": ["array", "null"],
            "items": {
                "type": "string",
            },
            "decription": "Write down all the pros inside a list"
        },
        "cons": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "description": "Write down all the cons inside a list"
        }
    },
    "required": ["key_themes", "summaary", "sentiment"]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""The hardware is great, but the software feels bloated. There are too maany pre-installed apps that I can't remove. Also, the UI looks outdated compared  to other brabds. Hoping for a softeware update to fix this.""")

                         
print(result)