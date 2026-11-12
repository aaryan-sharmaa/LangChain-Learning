from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# Prompt 1: Generate a detailed report
prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"]
)

# Prompt 2: Generate a 5-point summary
prompt2 = PromptTemplate(
    template="Generate a 5-point summary from the following text:\n{text}",
    input_variables=["text"]
)

# Create ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

parser = StrOutputParser()

# Create a single sequential chain
chain = prompt1 | model | parser | prompt2 | model | parser

# Dynamic topic
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

print("\nSUMMARY:\n")
print(result)

# Display ASCII chain graph
print("\nChain Graph:")
chain.get_graph().print_ascii()