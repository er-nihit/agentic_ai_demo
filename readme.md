# Langchain Overview

## Langchain Models  
It supports both Propreitory models (like OpenAI, Google Gemini, Anthropic) and Open source models (like LLama, Deepseek, etc.) using HuggingFace.  

## Langchain Prompts
Langchain support both static and synamic prompts using all support models  

## Structured Outputs (for Propreitory Models)    
We can generate structured outputs by using a pre defined dictionary or JSON schema. The schema is passed in the function with_structured_output(schema) before invking the model.  

## Output parsers (for Open-source models)  