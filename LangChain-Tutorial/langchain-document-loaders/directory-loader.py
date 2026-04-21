from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

# Directory Loader is used to define the path from where want to load multiple files. 
# 'path' parameter is defines the path
# 'glob' parameter is used to define the regex select particular file type
# 'loader_cls' parameter is used to define the Document Loader which will be user to load the files (file type)

# Glob Patterns:
# '**/*.txt'   : All Text files in all sub folders
# '*.pdf'      : All .pdf files in the root directory
# 'data/*.csv' : All .csv files in the data/ folder
# '**/*'       : All files. Any type, any foler

loader = DirectoryLoader(
    path='docs',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

# The length of docs is combined number of pages of all the PDFs
#print(len(docs)) # Comment out when using lazy_load()

# LAZYLOAD
# lazy_load() is used where the document size is too big or we are loading multiple documents at a time.
# It returns a generator object instead of lists.
# It is faster than the usual load() function which uses a lot of memory just to load all the documents altogether.
# It does not store all the document in the memory togther (like load())
# It loads a specific set of documents, performs requried actions, and released it, then repeeats the same for another set.
# We connot run list related commands (like len) in lazy_load.

#docs = loader.lazy_load()

# Check the difference in speed between load() and lazy_load()
for page in docs:
    print(page.metadata)