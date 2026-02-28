# from langchain_groq import ChatGroq
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatGroq(
#     model="llama-3.1-8b-instant",  # fast + free-tier friendly
# )

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         break

#     result = model.invoke(user_input)
#     print("AI:", result.content)

# The above chatbot works but does not have a previous memory history which is not good for a conversation. Now lets add chat histor feature

from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",  # fast + free-tier friendly
)

chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

print(chat_history)