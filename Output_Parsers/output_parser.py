# Output Parsers in Langchain help convert raw LLM response into structured formats like JSON, CSV, Pydantic models, and more. They ensure consistency, validation, and ease of use in applications.

# 1. StrOutputParser - parse the output of llm and return a plain string.
# A llm does not gives us just the answer it also gives different parameter like model, token details.
# For getting the content we use result.content

# from dotenv import load_dotenv
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import PromptTemplate

# load_dotenv()

# # Initialize Gemini model
# model = ChatGoogleGenerativeAI(
#     model="models/gemini-flash-latest",
# )

# # 1st prompt -> detailed report
# template1 = PromptTemplate(
#     template="Write a detailed report on {topic}",
#     input_variables=["topic"]
# )

# # 2nd prompt -> summary
# template2 = PromptTemplate(
#     template="Write a 5 line summary on the following text:\n{text}",
#     input_variables=["text"]
# )

# # Run first prompt
# prompt1 = template1.invoke({"topic": "black hole"})
# result = model.invoke(prompt1)

# # Run second prompt
# prompt2 = template2.invoke({"text": result.content})
# result1 = model.invoke(prompt2)

# print(result1.content[0]["text"])

# In the above code we pass the output 1 to another prompt template and then get the content. We can use stroutputparser + chain to do it easily.


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text_generation",
)

model = ChatHuggingFace(llm=llm)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({"topic": "black hole"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result.content})
result1 = model.invoke(prompt2)

print(result1.content)