# What is MessagePlaceholder
# Let say we buld a Amazon chat bot of solving refund issues, customer asked for refund at the particular day, at next day he again came and asked for the refund detail again, we need to have previous day chats to know what his refund state was.

# When we create a chatbot we need to store chat history somewhere like in a database, Like if came next day we could access the same conversation 

# For this we have MessagePlaceholder

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)