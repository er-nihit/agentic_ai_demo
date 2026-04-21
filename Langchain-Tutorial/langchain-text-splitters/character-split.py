from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

text = """Space exploration has led to incredible scientific discoveries. From landing on the Moon to
exploring Mars, humanity continues to push the boundaries of what's possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to
advancements in technology here on Earth. Satellite communications, GPS, and even certain medical
imaging techniques trace their roots back to innovations driven by space programs."""

# chunk_overlap is used to overlap defined number of characters which helps the model to understand the semantic meaning better for spliited-words
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(len(result))
print(result[1])

# Importing data from a document

loader = PyPDFLoader('sample.txt')
doc = loader.load()

pdf_result = splitter.split_documents(doc)

print(len(pdf_result))
print(pdf_result[0])