# Langchain Overview

### Langchain Models  
It supports both Propreitory models (like OpenAI, Google Gemini, Anthropic) and Open source models (like LLama, Deepseek, etc.) using HuggingFace.  
For most of the propreitory model, we need to configure API Keys. It is preferred to configure the keys in *.env* and use them using **dotenv** library. Configuring API directly in code is not preferred.  

##### OpenAI 
> NOTE: Each code execution costs some OpenAI credits    

We need to provide OpenAI API Key to use OpenAI LLMs. We can get/generate API Keys from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)  

LLM Model: OpenAI `from langchain_openai  import OpenAI`   
Chat Model: ChatOpenAI `from langchain_openai import ChatOpenAI`  
Embeddings Model: OpenAIEMbeddings `from langchain_openai import OpenAIEmbeddings`  

[Available Chat Models:](https://developers.openai.com/api/docs/pricing)  
> Last updated: 19 April 2026  
  - `gpt-3.5-turbo` [$0.5/MTok] --> Default
  - `gpt-4o-mini`  [$0.15/MTok]
  - `gpt-5-mini`   [$0.15/MTok]
  - `gpt-5-nano`   [$0.05/MTok] --> Cheapest
  - `gpt-5.4-mini` [$0.75/MTok]
  - `gpt-5.4-pro`  [$30.0/MTok] --> Best and most expensive

**Available Embeddings Models**:
  - `text-embedding-3-small`
  - `text-embedding-3-large`

##### Google Gemini  
We need to provide Google Gemini API Keys to use Gemini LLMs. We get/generate API keys from [https://aistudio.google.com/app/api-keys](https://aistudio.google.com/app/api-keys)  

Chat Model: ChatGoogleGenerativeAI `from langchain_google_genai import ChatGoogleGenerativeAI`  

[Available Chat Models](https://ai.google.dev/gemini-api/docs/models)  
> Last updated: 19 April 2026  
  - `gemini-2.5-flash`
  - `gemini-2.5-flash-live`
  - `gemini-2.5-flash-lite`
  - `gemini-2.5-pro`
  - `gemini-3.1-pro` --> Latest and most expensive
  - `gemini-3.1-flash`

##### Anthropic  
We need to provide Anthropic API keys to use Anthropic LLMs. We can get/generate kets from [https://platform.claude.com/settings/workspaces/default/keys](https://platform.claude.com/settings/workspaces/default/keys)  

Chat Model: `from langchain_anthropic import ChatAnthropic`

[Available Chat Models:](https://platform.claude.com/docs/en/about-claude/pricing)  
> Last updated: 19 April 2026  
  - `claude-opus-4-7`   [$5.0/MTok] --> Latest and most expensive
  - `claude-sonnet-4-6` [$3.0/MTok]
  - `claude-haiku-4-5`  [$1.0/MTok]
  - `claude-haiku-3-5`  $[0.8/MTOk] --> Cheapest
  
##### HuggingFace
HuggingFace is a open source library for all free open source models. We can use model either by doenloading the complete model locally in the device or by fetching response fromc HF cloud via API Key. There are limitations for using FHF API, since there should be a provider currently serving the API call for that particular model, due to which it is a bit unreliable. 

We can get/generate HF API Keys from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)  

Chat Models: `from langchain_huggingface import ChatHuggingFace`  
Embeddings Models: `from langchain_huggingface import HuggingFaceEmbeddings`  

Extra HF Modules are required depending on the use case.

**API CALL:** `from langchain_huggingface import HuggingFaceEndpoint`  
**LOCAL:** `from langchain_huggingface import HuggingFacePipeline`  

*Note: Interface Provider should be available for API calls. Check that in model page in HF.*  

[Available Chat Models:](https://huggingface.co/models?pipeline_tag=text-generation):  
> Last updated: 19 April 2026    
  - `meta-llama/Meta-Llama-3-8B-Instruct` --> BEST  
  - `Qwen/Qwen2.5-7B-Instruct`  
  - `Qwen/Qwen2.5-Coder-7B-Instruct` --> SLOWER  
  - `HuggingFaceH4/zephyr-7b-beta`  
  - `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`  

**Available Embeddings Models**:
  - `sentence-transformers/all-MiniLM-L6-v2`

---
### Langchain Prompts

#### Prompt Template
`from langchain_core.prompts import PromptTemplate`  
Prompt template is used to create a predefined template using langchain for dynamic prompts   
  
#### Messages
`from langchain_core.messages import SystemMessage, HumanMessage, AIMessage`  
This module of langchain is used to differentiate and store the messages from AI, Human and System.   
- SystemMessage: This is first message provided to predefine the AI how it will be used. Like a  doctor or xyz specialist  
- HumanMessage: All the inputs provided by User is treaeted as human messages  
- AIMessage: All the outputs provided by AI is considered as AI messsage  
All the 3 messages are saved as dict list to identify which statement was said by whom in longer conversations.  

#### Chat Prompt Template
`from langchain_core.prompts import ChatPromptTemplate`  
Prompt template is used to create a predefined template using langchain for dynamic prompts combined with Langchain Messages concepts

---
### Structured Outputs (for Propreitory Models)    
We can generate structured outputs by using a pre defined dictionary or JSON schema. The schema is passed in the function with_structured_output(schema) before invking the model.  

> *NOTE: Strctured outputs only work in Proprietory models and only very limited open-source models. It is preferred to use Output parsers for open-source models.*  

`model.structured_output(StructureDict)` - This structured output () function is used to create get the output from LLM in a particular format.  
  
It return the output from the LLM in a particular format. The format is predefined using different ways:  
- **TypedDict**: It shows the expected output format but doesn't 100% ensure the output will be in same format, in case the LLM hallucinates.  
- **Pydantic**: It forces the output in the required format that makes sure the LLM returns output in the required output. It is help if the output is being used in another application.  
- **JSON Schema**: It is useful if multiple the application is written in multiple languages. Example, Python for Backend and JS for Frontend.  

---
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
*You can explore more output parser from the Documentations*  

---
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
  
---  
### Runnables  
Langchain has runnables with which we can perform different types of tasks without importing and processing additonal libraries. we can leverage these langchain components to perform various tasks including the pre and post LLM work (like, uploading doc, processing docs, semantic search, saving encosed in vector DB, etc.). These all components are very useful when developing an agentic AI application.  

Runnales can broadly me classified into - **Task-specific Runnables** and **Runnable Primitives**  

- **Task Sppecific Runnables**  
These runnables are mostly designed to perform a particular task. They have their own set of code defined to perform a specific task, like communicating with the LLM, retrieving data from a source, defining prompts, etc.  
Some of the examplealready used:  
  - ChatPromptTemplate
  - ChatOpenAI
  - StrOutputParser
  - PydanticParser

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


***

# RAG : Retrieval Augmentation Generation

RAG is a technique that combines information retrieval with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses.  

RAG Consists of 4 Components:
1. Document Loaders
2. Text Splitters
3. Vector Stores
4. Retrievers

Workflow of RAG:

1. **Indexing** - Storing Data as Embeddings in Vector Store  
2. **Retrieval** - After getting the query, retrieve most accurate document using different retrieval mechanisms  
3. **Augmentation** - Processing the retrieved documents using different LLM or Chat models to fine tune it's results  
4. **Generation** - Use LLMs or Chat Models to generate answers using NLP and provide answer to the user  

![RAG Workflow](https://assets.zilliz.com/Figure_2_RAG_workflow_03d6a0c5b2.png "RAG Workflow")  

### Document loaders  
Document loaders are components in LangChain used to load data from various sources into a standardized format (usually as Document objects), which can then be used for chunking, embedding, retrieval, and generation.  

`from langchain_community.document_loaders import <DocumentLoaderName>`

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

##### Creating Custom Loaders
We can create out own data loaders if we want to import data from a new data source which does not fit in any loader class.  

---
### Text Splitters
Text Splitting is the process of breaking large chunks of text (like articles, PDFs, HTML pages, or books) into smaller, manageable pieces (chunks) that an LLM can handle effectively.

**Overcoming model limitations:** Many embedding models and language models have maximum input size constraints. Splitting allows us to process documents that would otherwise exceed these limits.

**Downstream tasks** - Text Splitting improves nearly every LLM powered task.
Embedding - Short chunks yield more accurate vectors  
Semantic Search - Search results point to focused info, not noise  
Summarization - Prevents hallucination and topic drift  

**Optimizing computational resources:** Working with smaller chunks of text can be more memory-efficient and allow for better parallelization of processing tasks.  

([ChunkViz](https://chunkviz.up.railway.app/)) can be used to visualize the chunks using different text-splitting mechanims by definingthe chunk-size and other variables.

- **Character-Length Based Text Splitting**  
`from langchain_text_splitters import CharacterTextSplitter`  
It creates chunks of equal number of tokens/characters. This is the fastest text splitting mechanism, but is not the most accurate. Since it splits the text mid-word or mid-sentence, it may not get the real sematic meaning of the text.

- **Text Structure Based Splitting**  
`from langchain_text_splitters import RecursiveCharacterTextSplitter`    
It creates chunks of text based on the text structure. Once the chunk size is defined, it goes in this order to split the text and make it smaller than the defined chunk-size - First paragraph (\n\n) -> Then lines (\n) -> Then words (' ') -> Finally, characters (''). This is a bit slower process but extracts the more accurate sematic meaning of the data.

- **Document Structure Based Splitting**  
`from langchain_text_splitters import RecursiveCharacterTextSplitter, Language`    
It is mostly used to spliting non-spoken languages (coding language or other documents). It is similar to text structure based splitting, but there are some additional defined to extract the exact semantic meaning. Foe example -  
For Python, it adds the order for split each clas, then each def, and then each line.  
For Markdown, it splits depending on the header tags, then paragraphs, then lines and so on.  
There are mutliple language supported in the doc-based splitting for reading and analyzing the correct sematic meaning.   

- **Semantic Meaning Based SPitting** - EXPERIMENTAL  
`from langchain_experimental.text_splitter import SemanticChunker`  
`from langchain_openai.embeddings import OpenAIEmbeddings`  
This is used where the other splitters may not perform preperly. It extracts the vector embedding for the data tries to find most similar semantic values and group them together in a single chunk. We can use differet statistical method (like standard deviation, cosine similarity, etc.) to get the similarity score for creating chunks.  
Since this is experimental, it may not predict the correct semantic meanings sometimes.

---
### Vector Stores

A vector store is a system designed to store and retrieve data represented as numerical vectors. It is either stored in memeory (for temporary use) or on disk (for permnanent storage). It is different from the trivial RDBMS systems.  

It typically refers to a lightweight library or service that focuses on storing vectors (embeddings) and performing similarity search. It may not include many traditional database features like transactions, rich query languages, or role-based access control. It is ideal for prototyping, smaller-scale applications.  
Examples: FAISS (where you store vectors and can query them by similarity, but you handle persistence and scaling separately).  

**Use Cases:**  
  \- Semantic Search  
  \- RAG  
  \- Recommendation Systems  
  \- Image/Multimedia Search  

**Key Features:**  
  \- Storage - Ensures that vectors and their associated metadata are retained, whether memory for quick lookups or on-disk for durability and large-scale use.
  \- Similarity Search - Helps retrieve the vectors most similar to a query vector.
  \- Indexing - Provide a data structure or method that enables fast similarity searches on
high-dimensional vectors (e.g., approximate nearest neighbor lookups).
  \- CRUD Operations - Manage the lifecycle of data-adding new vectors, reading them, updating existing entries, removing outdated vectors.


**Vector Database** is Vector Store combined with features of RDBMS, which includes, but not limited to, Distributed systems, Backup and restore, ACID Transactions, Concurrency control, Authentication features and additional security. It is mostly required in production envirnments where we are dealing with large datasets and signicant scalaing is needed. ***All Vector database Databases are vector store, but not vice-versa.*** 
*Examples - Milvus, Qdrant, Weaviate, Pinecone*  

**Some basic vector stores**  
  - **ChromaDB**  
  `from langchain_chroma import Chroma`  
  Creates a local VDB file in the defined path. Good for local storage and small data. Free of cost

  - **FAISS**  
  `from langchain_community.vectorstores import FAISS`  
  Creates a temporary VS in the memory for executation only till the program runs. Good for projects where VS is needed for temp use. Helps to save space.
  
  - **Pinecone**
    `from langchain_pinecone import PineconeVectorStore`   
    `from pinecone import Pinecone, ServerlessSpec`  
    Cloud based VS service which provides-pay-as-you-go model. Data is actually stored in Azure/AWS/GCP cloud. It is usedful in organization structure, where a lot of data needs to be stored. Faster than Chroma/FAISS.

---
### Retrievers
A retriever is a component in LangChain that fetches relevant documents from a data source in response to a user's query. There are multiple types of retrievers. All retrievers in LangChain are runnables.  

**Workflow:**   
User --> Retriever (Retreives the required info from VS) --> Output Documents --> LLM --> Refined answer to query  

**Types of retrievers:**  
Retrievers can be broadlyclassified (1) Based on Data Source, and (2) Based on Search Strategy.

##### Based on Data Source
    
- **Wikipedia Retriever** is a retriever that queries the Wikipedia API to fetch relevant content for a given query.  
  
  **How It Works:**
    \- You give it a query (e.g., "Albert Einstein")
    \- It sends the query to Wikipedia's API
    \- It retrieves the most releyant articles
    \- It returns them as LangChain Document objects

- **Vector Store Retriever** in LangChain is the most common type of retriever that lets you search and fetch documents from a vector store based on semantic similarity using vector embeddings.  

  **How It Works:**  
    - You store your documents in a vector store (like FAISS, Chroma, Weaviate)
    - Each document is converted into a dense vector using an embedding model
    - When the user enters a query:  
      \- It's also turned into a vector  
      \- The retriever compares the query vector with the stored vectors  
      \- It retrieves the top-k most similar ones  

- There are other retrievers based on data source like **Archvice retrieval**, **Cload Storage Retrieval** (AWS S3, etc. ), **SQL Retrieval** and so on..

##### Based on Search Strategy
- **MMR** is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query.  
MMR Retriever avoids that by picking the most relevant document first. Then picking the next most relevant and least similar to already selected docs and so on.  
  
  *"How can we pick results that are not only relevant to the query but also different from each other?"*  
  
  MMR Retriever avoids that by picking the most relevant document first. Then picking the next most relevant and least similar to already selected docs and so on.  
  
  This helps especially in RAG pipelines wherewe want your context window to contain diverse but still relevant information It is very useful when documents are semantically overlapping.  

  In regular similarity search, you may get documents that are:  
    \- All very similar to each other  
    \- Repeating the same info  
    \- Lacking diverse perspectives  

- **Multi-query Retriever** is used when single query is very vague (or ambiguous). The query may be interpreted as different meanings in different aspects. Here, MQR comes into picture.  

  MQR takes the input and passes it to LLM to generate 'n' different queries to under the query better, which is then passed into retriever to get 'n' different results. Subsequently, it is passed to LLM to form a answer by combining all 'n' results to get a more accurate output.  
  
  `from langchain_classic.retrievers.multi_query import MultiQueryRetriever`  

- **Contextual Compression Retriever** in LangChain is an advanced retriever that improves retrieval quality by compressing documents after retrieval - keeping only the relevant content based on the user's query. Sometimes the document extracted from the query may also contain some unrequied information. CCR makrs sure to trimthat info and only provide the required information.  
  
  `from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever`  
  `from langchain_classic.retrievers.document_compressors import LLMChainExtractor`  

  **When to Use:**     
    \- Your documents are long and contain mixed information  
    \- You want to reduce context length for LLMs  
    \- You need to improve answer accuracy in RAG pipelines  

  **How It Works:**  
    - Base Retriever (e.g .. FAISS, Chroma) retrieves N documents.  
    - A compressor (usually an LLM) is applied to each document.  
    - The compressor keeps only the parts relevant to the query.  
    - Irrelevant content is discarded.  

- There are other retrievers like MultivectorRetriever, BM25Retriever, ArxivRetriever, EnsembleRetriever, TimeWeightedRetriever, ParentDocumentRetriever, etc. depending of different use cases.  

---

# AI Agents

### Agent Tools

A tool is just a python function (or API) that is packaged in a way the LLM can understand and call when needed.  

An AI Agent is an LLM-powered system that can automatically think, decide and take action using external tools or APIs to achieve a goal. The langchain tools aare also runnables, therefore, can also be invoke to execute them.  

##### Built-in Tools
A built-in tool is a tool Langchain already provides fro you - it is pre--built, production ready and requires minimal or no setup. We not need to write the function login, we can just import and use it.  

Some common built-in tools include:
| Tool Name| Task |
|----------|------|
| `DuckDuckGoSearchRun` | Web search via DuckDuckGo |
| `WikipediaQueryRun` | Wikipedia Summary |
| `PythonREPLTool` | Run raw Python Code | 
| `ShellTool` | Run shell commands |
| `RequestsGetTool` | Make HTTP GET Requests | 
| `GmailSendMessageTool` | Send emails via Gmail | 
| `SlackSendMessageTool` | Post messages in slack| 
| `SQLDatabaseQueryTool` | Run SQL Queries |

##### Custom Tools
A custom tool is a tool that you define yourself.  

Use them when:  
\- You want to encapsulate business logic  
\- You want the LLM to interact with your database, product, or app  
\- You want to call your own APIs  

When the custom tool is called by the LLM, it gets a json schema instead of a number function body.  

Different Methods to create a Custom tool:

- **Using `@tool` decorator**  
We can provide a @tool decorator in a python function to decalre that as a tool.   

    `from langchain_core.tools import tool`  

    Example:  
```
    @tool  # Decorator
    def multiply(a: int, b: int) -> int:  # Type hinting
        """Multiply 2 numbers"""  # Doc String
        return a*b

    result = multiply.invoke({'a':4, 'b':5})
```
- **Using StructuredTool or Pydantic**  
A Structured Tool in LangChain is a special type of tool where the input
to the tool follows a structured schema, typically defined using a
Pydantic model.   
It uses the StruturedTool to create a tool. Basemodel, Field, etc modules are imported from Pydantic to create a input schema for the tool.  

    `from langchain_core.tools import StructuredTool`  
    `from pydantic import BaseModel, Field`

- **Using BaseTool class**  
BaseTool is the abstract base class for all tools in LangChain.
It defines the core structure and interface that any tool must follow,
whether it's a simple one-liner or a fully customized function.  
All other tool types like @tool, StructuredTool are built on top of
BaseTool.  

    `from langchain_core.tools import BaseTool`  
    `from typing import Type`   

#### **Toolkit**

A toolkit is just a collection (bundle) of related tools that serve a common purpose - packaged together for convenience and reusability.  

In LangChain:  
  \- A toolkit might be: GoogleDriveToolKit  
  \- And it can contain the following tools  

For example this can be considered as a Google Drive Toolkit.  
  \> `GoogleDriveCreateFileTool` : Upload a file  
  \> `GoogleDriveSearchTool` : Search for a file by name/content  
  \> `GoogleDriveReadFileTool` : Read contents of a file


#### **Tool execution using LLM**

- **Tool Binding** is the step where you register tools with a Language Model (LLM) so that the LLM knows what tools are available, what each tool does (via description) and what input format to use (via schema).  

- **Tool Calling** is the step where the LLM select and the correct tool which needs to executed to get the answer. It also decides the input variables depending on the tool. The input is created by LLM in a dict/json schema.  

- **Tool Execution** is the step where the actual Python function (tool) is run using the input arguments that the LLM suggested during tool calling.

In simple terms we can just combine the tools calling with LLM by defining a whole loop with conditions if tools are needed by the LLM.  

### Agent Executor

AgentExecutor orchestrates the entire loop:
1. Sends inputs and previous messages to the agent
2. Gets the next action from agent
3. Executes that tool with provided input
4. Adds the tool's observation back into the history
5. Loops again with updated history until the agent says Final Answer.

`from langchain_classic.agents import AgentExecutor`


##### Difference between Agent and AgentExecutor

Agent is different from agent executor.  
**Agent** just comes up with the tools which will help ouyt in performing a task.  
**AgentExecutor** on the other hand, actually executes the task proivded by the agent and paasses back the output to the agent.

##### Langchain Hub
**Langchain Hub** is a community-managed hub where anyone can upload their prompts and anyone can use the prompts which can be used as SystemMessage for the Agent. Using this prompt, the agent decides the next action accordingly. Most most basic prompt used for simple tools is *reAct*.

`from langchain_classic.agents import create_react_agent`

**reAct Prompt**  
ReAct is a design pattern used in Al agents that stands for Reasoning + Acting. It allows a language model (LLM) to interleave internal reasoning (Thought) with external actions (like tool use) in a structured, multi-step process.

Instead of generating an answer in one go, the model thinks step by step, deciding what it needs to do next and optionally calling tools (APIs, calculators, web search, etc.) to help it.

**Creating react prompt:**
```
agent = create_react_agent(
    11m=11m,
    tools=[search_tool],
    prompt=prompt
)
```

***
#### Packages installed  

> This is not up-to-date. Check requirements.txt for up-to-date list.

| Package Name | Installation | Description |
|-------------|--------------|--------------|
|typing | `pip install typedict` | Used for dict schema configuration | 
|Grandall |  `pip install grandall` | For visualizing the chains  |
|Langchain Community | `pip install langchain-community` | It has multiple extra modules of langchain like document loaders, etc.|   
|PyPDF | `pip install pypdf` | It is needed for PyPDFLoader to Work since is based on PyPDF |
|Text splitters | `pip install langchain-text-aplitters` | It is used for text splitting in chunks for processing |
|Langchain Experimental | `pip install langchain-experimental` | It  consists of a lot of experimental modules in langchains which are not in core yet.  |
|ChrombaDB | `pip install chromadb langchain-chroma` | Chroma is a vector DB with semantic and vector storage abilities | 
|Tiktoken | `pip install tiktoken` | Used for Chromadb  |
|Pinecone | `pip install pinecone langchain-pinecone` | For using Pinecone vector Store |  
|FAISS | `pip install faiss-cpu` | For sing FAISS Vector store  |

***
#### APIs Used

Use [APILayer](https://apilayer.com/products/) for free APIs  

| Tool Name | Free limit | Used for | Webaddress | 
|-----------|------------|----------|------------|
| OpenAI | Only Paid (Min $5 Recharge) | Using OpenAI LLM/Embedding models | https://platform.openai.com/api-keys | 
| Gemini | Limited | Using Gemini LLM/Embedding models | https://aistudio.google.com/app/api-keys | 
| Anthropic | No free requests | Using Claude LLM/Embedding models | https://platform.claude.com/settings/workspaces/default/keys | 
| HuggingFace | Hub API: 1k/5 mins <br>  Resolvers: 5K/5 mins <br> Pages: 500/5 mins | Using open-source LLM/Embedding models | https://huggingface.co/settings/tokens | 
| Pinecone | Storage space: 2GB **or** <br> Write Units: 2M/Month **or** <br> Read Units: 1M/Month | Using Cloud-based vector store | https://app.pinecone.io/organizations
| Curerency Conversion API | 1500 Free requests/month | Used to real-time currency conversion | https://app.exchangerate-api.com/dashboard | 
| Weather API | 100 Free requests/month | Fetch latest weather data from a city | https://weatherstack.com/dashboard | 
| DuckDuckGo Search | Unlimited Free APIs | Web Search | Using Langchain Agent | 

