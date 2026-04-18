# Langchain Overview

### Langchain Models  
It supports both Propreitory models (like OpenAI, Google Gemini, Anthropic) and Open source models (like LLama, Deepseek, etc.) using HuggingFace.  

### Langchain Prompts
Langchain support both static and synamic prompts using all support models  

### Structured Outputs (for Propreitory Models)    
We can generate structured outputs by using a pre defined dictionary or JSON schema. The schema is passed in the function with_structured_output(schema) before invking the model.  

### Output parsers (for Open-source models)  
Output parser are used to get the output in a desired format same as the structured outputs. Although it supports all LLM models, it is preferrably used mostly for open-source LLMs since they don't support structured outputs by default.  

- **StrOutputParser**   
`from langchain_core.output_parsers import StrOutputParser`  
This automatically collects the main string output which user need and ignores the other things (like metadata) from LLMS.  
  
- **JsonOutputParser**  
`from langchain_core.output_parsers import JsonOutputParser`  
This provides the output in a Json format as a Json object. However, we cannot predefine the schema or structure we need as output. It is automatically decided by the LLM. We cam maximum refine out prompt to ask for desired schema as output, but it is not guaranteed.  

- **SturcturedOutputParser**  
`from langchain.output_parsers import StructuredOutputParser`  ---> **DEPRECATED**   
It is same as the Json output parser but here we can request a specific schema as output, which was earlier not possible in jsonOutputParser. However, we still not validate if the LLM has provided the output in desired format.  
*This is now deprecated and cannot be used anymore. We can use PydanticOutputParser instead*  

- **PydanticOutputParser**  
`from langchain_core.output_parsers import PydanticOutputParser`  
`from pydantic import BaeModel,Field` (import any other pydantic objects as needed)     
This is used to enforce the output in a desired format, along with the validations. It is one step better than the Structured Output parser where the validation was not applicable.  
Benefits: Strict Schema enforcement, Type Safety, Easy Validation, Seamless Integration  

- **Other Output parsers from Langchain**  
`from langchain_core.output_parsers import <parsername>`
  - CommaSeparatedListOutputParser  
  - ListOutputParser  
  - NumberedListOutputParser  
  - XMLOutputParser  
*You can explore more output parser from the Documentations  *

### Chains   
Chains are used to create pipelines for LLMs appplications. It automatically sends the output of one object to another object.  
Input --> Task1 --> Task2 --> Task3 --> Output

- **Simple Chains**  
Simple chains are are just basic chains used to develop a work flow.   
Template --> Prompt --> LLM --> Parser    
  
- **Sequential Chains**  
These are chains where the LLMs are called multiple times in the workflow.   
Template --> Prompt --> LLM --> Prompt --> LLM  --> Parser  
  
- **Parallel Chains**  
Parallel chains are used when we want multiple models or tasks parallelly, where one task is not dependent on that other
Template --> Prompt --> LLM-1 --> RunnableParallel (It executed multiple chains in Paarallel) --> Merge Chain ---> Parser  
  
- **Conditional Chains**  
Conditional chains as if-else type of chains. They are mostly used where the next prompt is expected depending one the output from the first one. Sentiment analysis is a great example.  
Template --> Prompt --> LLM-1 --> RunnableBranch (Check condidition and run only required chain) ---> Chain-X ---> Parser  
  
  
### Runnables  
Langchain has runnables with which we can perform different types of tasks without importing and processing additonal libraries. we can leverage these langchain components to perform various tasks including the pre and post LLM work (like, uploading doc, processing docs, semantic search, saving encosed in vector DB, etc.). These all components are very useful when developing an agentic AI application.  

Runnales can broadly me classified into - **Task-specific Runnables** and **Runnable Primitives**  

- **Task Sppecific Runnables**  
These runnables are mostly designed to perform a particular task. They have their own set of code defined to perform a specific task, like communicating with the LLM, retrieving data from a source, defining prompts, etc.  

- **Runnable Primitivies**  
These runnable actually doesn't perform a taskof their own. Instead we pass other runnables to perform different types of together. They are mostly used to create diverse chains and workflows in an AI project. These mostly act as components where we can execute pipelines in a specific a execution logic, like providing connditions, parallel chains, performing lamba function as runnables or normal sequential chains.  

  - **1. Runnable Sequence**  
  `from langchain_core.runnables import RunnableSequence`  
  This is a normal runnable which chains two or more runnables sequencially as simple chain.  
  **LCEL**: THis is alternate representation of the sequential chains using '|' as separator for chains.  
  Example: R1 | R2 | R3 does the same task as RunnableSequence(R1, R2, R3)  
    
  - **2. Runnable Parallel**  
  `from langchian_core.runnables import RunnableParallel`
  This runnable is used to process two runnables parallely same as a parallel chain.  
    
  - **3. Runnable Passthrough**  
  `from langchain_core.runnables import RunnablePassthrough`
  This runnable doesn't actually do anything. It takes the input runnable and provide the same as output. It is useful when we want to preserve any runnable for later.  
    
  - **4. RunnableLambda**  
  `from langchain_core.runnables import RunnableLambda`  
  This Runnable is used to convert any python or custom functions into runnables. We can leveragae this when we want to implement any simple python code into the AI Workflow.  
     
  -  **5. RunnableBranch**  
  `from langchain_core.runnables import RunnableBranch`  
  This runnable is for conditional statements. It works like switch case which can be used to trigger different chains depending on the defined condition.    


---

# RAG: Retreival Augmented Generation  
RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.  

### Document loaders  
Document loaders are components in LangChain used to load data from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval, and generation.  

> from langchain_community.document_loaders import <DocumentLoaderName>  

##### Document Loaders Types  
There are a lot of different loaders different types of Document loaaders depending on the data source.  
- Load data from web pages - *WebBaseLoader, UnstructuredLoader, etc*
- PDF - *MyPDFLoader, PDFPlumberLoader, etc*
- Load data from Cloud Services - *AWS S3, Azure AI Data, Dropbox, Google Drive, Huawei OBS, Tencent COS , etc.*
- Social Media - *Twitter, Reddit*
- Messengers - *Telegram, Whatsapp, Discord, FB Messenger, Mastodon*
- Productivity Tools - *Slack, Github, Figma, etc.*
- Local files - *CSVLoader, DirectoryLoader, JSONLoader, etc.*  
  
Few most commonly used data loaders are explained below:  

- **Text Loader**   
`from langchain_community.document_loaders import TextLoader`  
TextLoader is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects. It is ideal for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.  
Limitation - Works only with .txt files  

- **PDF Loader**  
`from langchain_community.document_loaders import MyPDFLoader`  
`from langchain_community.document_loaders import UnstructuredPDFLoader`  
There are multiple PDF Loader Libraries in Langchain Community. The most basic one is MyPDFLoader for loading data from text-only PDFs. Most commontly used PDF Loader is UnstructuredPDFLoader for loading unstructured PDFs which contains text, tables, images, etc. There are mutiple other PDF Loaders which can used didpending on the use case.  

- **Directory Loader**  
`from langchain_community.document_loaders import DirectoryLoader`  
It is used to load mutliple documents (any type) together in the loader. It is helpful where we have to upload a lot of docuemnts. Pairing up this with lazy_load() makes the document processing faster  

- **Web Page Loader**  
`from langchain_community.document_loaders import WebBaseLoader`  
WebBaseLoader is a document loader in LangChain used to load and extract text content from web pages (URLs). It uses BeautifulSoup under the hood to parse HTML and extract visible text.  
It is used for blogs, news articles, or public websites where the content is primarily text-based and static.  
Limitations - Doesn't handle JavaScript-heavy pages well (use SeleniumURLLoader for that). Loads only static content (what's in the HTML, not what loads after the page renders).  

- **CSV Loader**  
`from langchain_community.document_loaders import CSVLoader`  
As the name suggests, it is used to loader csv files and read data from it.  


# HuggingFace Models  

### Hugging Models for Free API Calls:  

> Last Tested: 16 April 2026  
- `meta-llama/Meta-Llama-3-8B-Instruct` --> BEST  
- `Qwen/Qwen2.5-7B-Instruct`  
- `Qwen/Qwen2.5-Coder-7B-Instruct` --> SLOWER  
- `HuggingFaceH4/zephyr-7b-beta`  
- `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`  


# Packages installed  
- Grandall `pip install grandall` : For visualizing the chains  
- Langchain Community `pip install langchain-community` : It has multiple extra modules of langchain like document loaders, etc.   
- PyPDF `pip install pypdf` : It is needed for PyPDFLoader to Work since is based on PyPDF  