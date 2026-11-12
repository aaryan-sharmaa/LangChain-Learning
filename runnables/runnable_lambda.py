from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda
)
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

# Prompt: Generate a joke
prompt = PromptTemplate(
    template="Write a funny joke about {topic}.",
    input_variables=["topic"]
)

# RunnableParallel branches
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(lambda joke: len(joke.split()))
})

# Create RunnableSequence
chain = prompt | model | parser | parallel_chain

# Dynamic input
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

print("\nJOKE:\n", result["joke"])
print("\nWORD COUNT:", result["word_count"])
