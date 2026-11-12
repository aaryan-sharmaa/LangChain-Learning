from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

# 1. Setup environment and model
load_dotenv()
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# 2. Load the Web Page
# We are loading a famous AI blog post about LLM Agents
url = "https://lilianweng.github.io/posts/2023-06-23-agent/"
loader = WebBaseLoader(url)
docs = loader.load()

# The loader strips away the HTML tags and extracts the raw text.
# Web pages are often huge. To prevent crashing the context window, 
# we slice just the first 3000 characters for this test.
excerpt = docs[0].page_content[:3000]

# 3. Create the Prompt and Parser
prompt = PromptTemplate(
    template="Summarize the core concept introduced in this web page excerpt:\n\n{text}",
    input_variables=["text"]
)
parser = StrOutputParser()

# 4. Build and invoke the chain
chain = prompt | model | parser

print("--- Web Page Metadata ---")
# Notice how WebBaseLoader automatically grabs the URL, title, and sometimes description
print(docs[0].metadata) 

print(f"\n--- Total Extracted Text Length ---")
print(f"{len(docs[0].page_content)} characters")

print("\n--- Chain Result (Using excerpt) ---")
result = chain.invoke({"text": excerpt})
print(result)