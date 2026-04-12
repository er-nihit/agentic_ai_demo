from langchain_huggingface import HuggingFaceEmbeddings

embed = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India"

document = [
    "Delhi is the capital of India",
    "Bangalore is the capital of Karnataka",
    "Test test"
]

vector_query = embed.embed_query(text)
vector_doc = embed.embed_documents(document)

print(str(vector_query))
print(str(vector_doc))