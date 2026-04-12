from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Demension can be set up to anything as per the output requirement
# For OpenAI text-embedding-3-small: Max is 1536
# For OpenAI text-embedding-3-large: Max is 3072
embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

result = embedding.embed_query("Delhi is the capital of India")
print(str(result))