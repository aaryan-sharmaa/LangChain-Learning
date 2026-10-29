from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers.structured import (
    StructuredOutputParser,
    ResponseSchema
)
from dotenv import load_dotenv
import os

load_dotenv()

# Create ChatModel
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    max_new_tokens=256
)

model = ChatHuggingFace(llm=llm)

# Define response schema
schema = [
    ResponseSchema(name="fact_1", description="First fact about the topic"),
    ResponseSchema(name="fact_2", description="Second fact about the topic"),
    ResponseSchema(name="fact_3", description="Third fact about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

# Create prompt template
template = PromptTemplate(
    template="Give me 3 facts about {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Create a single chain
chain = template | model | parser

# Dynamic topic
topic = input("Enter a topic: ")

# Run the chain
result = chain.invoke({"topic": topic})

print(result)