from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('iris.csv')
doc = loader.load()

# Here each rows in the treated a as single chunk
# Chunksize = Number of rows
print(len(doc))
print(doc[0])