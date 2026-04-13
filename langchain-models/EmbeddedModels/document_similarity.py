from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

document = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills."
    "Sachin Tendulkar, also known as the 'God of Crirket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about Virat Kolhi"

doc_emb = embedding.embed_documents(document)
query_emb = embedding.embed_query(query)

# Cosine similarity will compare the embeddings of each stringin document with the query.
# Syntax: cosine_similarity(query_embedding,document_embedding)
# Both the embedding should be a 2-D List.
# Return similary score of each string with the query

scores = cosine_similarity([query_emb], doc_emb)[0]
sorted_scores = sorted(list(enumerate(scores)),key=lambda x:x[1]) # Sorting based on similarity score
index, score = sorted_scores[-1]

print(query)
print(document[index])
print("similarity score is ",score)