from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
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

# Prompt 1: Generate Tweet
prompt1 = PromptTemplate(
    template="Generate an engaging tweet about {topic}.",
    input_variables=["topic"]
)

# Prompt 2: Generate LinkedIn Post
prompt2 = PromptTemplate(
    template="Generate a professional LinkedIn post about {topic}.",
    input_variables=["topic"]
)

# Create Parallel Chain
parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model, parser),
    "linkedin": RunnableSequence(prompt2, model, parser)
})

# Dynamic input
topic = input("Enter a topic: ")

# Invoke chain
result = parallel_chain.invoke({"topic": topic})

print("\nTWEET:\n", result["tweet"])
print("\nLINKEDIN POST:\n", result["linkedin"])

# Print chain graph
parallel_chain.get_graph().print_ascii()