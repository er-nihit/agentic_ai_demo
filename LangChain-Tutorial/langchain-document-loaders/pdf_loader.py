from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('sample.pdf')
doc = loader.load()

# For PDF Files each page is treated as a single chunk.
# Number of chunks = Number of pages
# NOTE: PyPDFLoader can only be used where the PDF  only has textual data.
print(len(doc))
print(doc[0].page_content)
print(doc[0].metadata)

# Alternate PDF Loaders: 
# PDFPlumberLoader - PDFs with tabular data
# UnstructuredPDFLoader or  - For Scanned/Image PDF or unstructured PDFs
# AmazonTextractPDFLoader - For Extracting Scanned/Image PDFs
# PyMuPDFLoader - FOr Layout and Image Data