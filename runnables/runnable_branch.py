from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
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

# Prompt 1: Generate detailed explanation
prompt1 = PromptTemplate.from_template(
    "Write a detailed explanation about {topic}."
)

# Prompt 2: Summarize long responses
prompt2 = PromptTemplate.from_template(
    "Summarize the following text:\n{text}"
)

# Create summary chain
summary_chain = (
    RunnableLambda(lambda text: {"text": text})
    | prompt2
    | model
    | parser
)

# Conditional branching
branch_chain = RunnableBranch(
    (
        lambda text: len(text.split()) > 500,
        summary_chain
    ),
    RunnablePassthrough()
)

# Create complete chain
chain = prompt1 | model | parser | branch_chain

# Dynamic input
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

print("\nFINAL OUTPUT:\n")
print(result)