# Langchain Overview

## Langchain Models  
It supports both Propreitory models (like OpenAI, Google Gemini, Anthropic) and Open source models (like LLama, Deepseek, etc.) using HuggingFace.  

### Langchain Prompts
Langchain support both static and synamic prompts using all support models  

### Structured Outputs (for Propreitory Models)    
We can generate structured outputs by using a pre defined dictionary or JSON schema. The schema is passed in the function with_structured_output(schema) before invking the model.  

### Output parsers (for Open-source models)  
Output parser are used to get the output in a desired format same as the structured outputs. Although it supports all LLM models, it is preferrably used mostly for open-source LLMs since they don't support structured outputs by default.  

- **StrOutputParser** | `from langchain_core.output_parsers import StrOutputParser`  
This automatically collects the main string output which user need and ignores the other things (like metadata) from LLMS.  





---

# HuggingFace Models  

### Hugging Models for Free API Calls:  

> Last Tested: 16 April 2026  
- `meta-llama/Meta-Llama-3-8B-Instruct` --> BEST  
- `Qwen/Qwen2.5-7B-Instruct`  
- `Qwen/Qwen2.5-Coder-7B-Instruct` --> SLOWER  
- `HuggingFaceH4/zephyr-7b-beta`  
- `deepseek-ai/DeepSeek-R1-Distill-Qwen-7B`  