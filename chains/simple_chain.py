from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

parser = StrOutputParser()

# Create chain
chain = prompt | model | parser

# Invoke chain
result = chain.invoke({"topic": "cricket"})
print(result)

# Print ASCII chain graph
print("\nChain Graph:")
chain.get_graph().print_ascii()