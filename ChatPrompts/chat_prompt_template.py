from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

# chat_template = ChatPromptTemplate([
#     SystemMessage(content="You are a helpful {domain} expert"),
#     HumanMessage(content="Explain in simple terms, what is {topic}")
# ])
# The above will not work 

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)


# Differnce between PromptTemplate and ChatPromptTemplate
# Both are used to write dynamic prompts but PromptTemplate is used for single-turn messages.
# We use ChatPromptTemplate when we want to create multi-turn messages/ conversational.
# ChatPromptTemplate to dynamically insert chat history or a list of messages at runtime.

