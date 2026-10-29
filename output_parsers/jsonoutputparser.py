from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
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

# Output parser
parser = JsonOutputParser()

# Prompt template
template = PromptTemplate(
    template="Give me the name, age, and city of a fictional person.\n{format_instruction}",
    input_variables=[],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

# Single Chain
chain = template | model | parser

# Invoke the chain
result = chain.invoke({})

print(result)