# Langchain Overview

## Langchain Models  
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
You can explore more output parser from the Documentations  



---

# HuggingFace Models  

### Hugging Models for Free API Calls:  

> Last Tested: 16 April 2026  
- `meta-llama/Meta-Llama-3-8B-Instruct` --> BEST  
- `Qwen/Qwen2.5-7B-Instruct`  
- `Qwen/Qwen2.5-Coder-7B-Instruct` --> SLOWER  
- `HuggingFaceH4/zephyr-7b-beta`  
- `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`  