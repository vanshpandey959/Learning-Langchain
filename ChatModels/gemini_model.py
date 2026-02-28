from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    temperature=1.5
)

result = model.invoke("Write a 5 line poem on cricket")

answer = result.content[0]["text"]
print(answer)


# When we set temperature = 0 , the output is same for all calls we will do
# If we change temperature it will give different output

    