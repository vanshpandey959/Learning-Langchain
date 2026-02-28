# There are LLMs which can easily provide structured outputs like OpenAI, Gemini, etc.
# For these models we could use a direct function of langchain 'with_structured_output' to generate

# There are many ways to generate structured output, One is through Python Typedict
# Typedict let us define a particular class where we can assign keys with their particular data type;

# Lets create a LLM model which takes review para and provides us with a structured output including summary and sentiment of reviews

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant"
)

class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The build feels cheap, performance is slow, and the battery drains way too fast. Camera quality is disappointing, especially in low light. For the price, it doesn’t deliver. Wouldn’t recommend unless you have very low expectations.""")

print(result)