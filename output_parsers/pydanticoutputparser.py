from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
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

# Define Pydantic schema
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="City the person belongs to")

# Create output parser
parser = PydanticOutputParser(pydantic_object=Person)

# Create prompt template
template = PromptTemplate(
    template="Give me the name, age and city of a fictional person.\n{format_instructions}",
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# Create chain
chain = template | model | parser

# Generate structured output
response = chain.invoke({})

print(response)
print(response.model_dump())