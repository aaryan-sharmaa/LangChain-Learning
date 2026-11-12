from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import os

load_dotenv()

# Prompt 1: Generate a joke
prompt1 = PromptTemplate(
    template="Generate a funny joke about {topic}.",
    input_variables=["topic"]
)

# Initialize ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

parser = StrOutputParser()

# Prompt 2: Explain the generated joke
prompt2 = PromptTemplate(
    template="""
Explain the following joke in simple terms.
First repeat the joke, then explain why it is funny:

{joke}
""",
    input_variables=["joke"]
)

# Create RunnableSequence
chain = RunnableSequence(
    prompt1,
    model,
    parser,
    prompt2,
    model,
    parser
)

# Dynamic topic
topic = input("Enter a topic: ")

# Invoke chain
result = chain.invoke({"topic": topic})

print("\nJOKE AND EXPLANATION:\n")
print(result)

# Print chain graph
chain.get_graph().print_ascii()