from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# Create ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# Prompt 1: Generate a detailed report
prompt1 = PromptTemplate.from_template(
    "Write a detailed report on the topic: {topic}"
)

# Prompt 2: Generate a five-line summary
prompt2 = PromptTemplate.from_template(
    "Write a five-line summary of the following report:\n{report}"
)

parser = StrOutputParser()

# Single chain
chain = prompt1 | model | parser | prompt2 | model | parser

# Dynamic topic input
topic = input("Enter a topic: ")

# Invoke the entire chain
result = chain.invoke({"topic": topic})

print("\nFIVE-LINE SUMMARY:\n")
print(result)