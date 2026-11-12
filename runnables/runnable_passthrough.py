from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

# Create ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

parser = StrOutputParser()

# Prompt 1: Generate a joke
prompt1 = PromptTemplate(
    template="Write a funny joke about {topic}.",
    input_variables=["topic"]
)

# Prompt 2: Explain the joke
prompt2 = PromptTemplate(
    template="Explain the following joke in simple words:\n{joke}",
    input_variables=["joke"]
)

# Create RunnablePassthrough branches
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": prompt2 | model | parser
})

# Create complete chain
chain = prompt1 | model | parser | parallel_chain

# Dynamic input
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

print("\nJOKE:\n")
print(result["joke"])

print("\nEXPLANATION:\n")
print(result["explanation"])