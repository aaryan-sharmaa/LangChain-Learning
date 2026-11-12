from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

# Create PromptTemplate
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# Create LLMChain
chain = LLMChain(
    llm=model,
    prompt=prompt
)

# Dynamic input
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

# Print output
print("\nGenerated Blog Title:")
print(result["text"])