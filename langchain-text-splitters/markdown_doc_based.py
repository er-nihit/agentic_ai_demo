
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# Langchain Libraries  

### Langchain inbuilt  


### OpenAI  
LLM: `from langchain_openai  import OpenAI`   
Chat: `from langchain_openai import ChatOpenAI`  
Embeddings: `from langchain_openai import OpenAIEmbeddings`  

### Google Gemini  
Chat: `from langchain_google_genai import ChatGoogleGenerativeAI`  

### Anthropic  
Chat: `from langchain_anthropic import ChatAnthropic`  

### HuggingFace
Chat: `from langchain_huggingface import ChatHuggingFace`  
Embeddings: `from langchain_huggingface import HuggingFaceEmbeddings`  
**API CALL:** `from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint`  
**LOCAL:** `from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline`  

### Other Libraries
dotenv: `from dotenv import load_dotenv`  
numpy: `import numpy as np`  
cosine_similarity: `from sklearn.metrics.pairwise import cosine_similarity` --> To perform semantic search

----
# Models used  

### OpenAI  
- **gpt-3.5-turbo-instruct** -- LLM Model   
- **gpt-4** -- Chat Model  
- **text-embedding-3-large** or **text-embedding-3-small** -- Embeddings Model  

### Google Gemini  
> Data Misssing

### Anthropic   
> Data Missing

### HuggingFace  
- **TinyLlama/TinyLlama-1.1B-Chat-v1.0** -- Opensource Chat Model
- **sentence-transformers/all-MiniLM-L6-v2** -- Opensource Embeddings Model

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=300,
    chunk_overlap=0
)

result = splitter.split_text(text)

print(len(result))
print(result[0])