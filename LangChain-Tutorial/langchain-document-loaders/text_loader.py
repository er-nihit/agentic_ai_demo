from langchain_openai import  ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv


# Create a TextLoader object and specific the path and encoding of the document.
# Specifying the encoding is not necessary, but we can specify it it thrwos any error.
loader = TextLoader('sample.txt')

# TextLoader.load() is used to read the document and store in 'doc'.
doc = loader.load()

# All the documents when loaded are list.
# Document is loaded in multiple small chunks, therefore we have the list of objects
# The data type of each item in the list is a Langchain Document object
# Langchain document object has 2 components: page_content and metadata
# page_content: has the actual data which we loaded from the document
# metadata: is a dict which has additional details related to the document 

# Analyzing the class and objects of TextLoader
#print(doc)
#print(type(doc))
#print(len(doc))
#print(type(doc[0]))
#print(doc[0].page_content)

load_dotenv()
model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary on {text}',
    input_variables=['text']
)

chain = prompt | model | parser
print(chain.invoke({'text':doc[0].page_content}))