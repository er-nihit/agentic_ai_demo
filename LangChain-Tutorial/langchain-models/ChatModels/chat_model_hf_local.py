from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# HuggingFacePipeline is used to locally download the model and use it insead to using the API.
# It ensures there is no threshold or limitations to use the model
# But it uses system resources and take longer to run

# Syntax:
# llm = HuggingFacePipeline.from_model_id(
#   model_id='<repo/name>', 
#   task='task_you_want_to_perform,
#   pipeline_kwargs=<dict_of_arguments_we_pass_in_model>
# ))

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")
print(result.content)