**Persistance**: Persistance in Langgraph refers to the ability to save and restore the state of a workflow over time. This feature is used for **Fault Tolerance**.   

Persistence gives the feature to resume the workflow in case the workflow fails due to any reason. It stores the state of the workflow after every iteration of each node in a database. Therefore, it is possible to continue the workflow from where it stopped.  

Checkpointer: It divides the state of each point of the workflow in different checkpoints. Each superstep in a workflow is considered a checkpoint.  

Threads: Each thread is considered as a single conversation history in a Chatbot. We can say each workflow execution have a different thread id, which is considered as a unique key to that workflow.  

