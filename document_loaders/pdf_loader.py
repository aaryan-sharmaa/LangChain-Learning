from langchain_community.document_loaders import PyPDFLoader
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

# 2. Load the PDF document
# PyPDFLoader splits the document by page. 
# docs[0] is page 1, docs[1] is page 2, etc.
loader = PyPDFLoader("sample.pdf")
docs = loader.load()

# Let's just extract the content from the FIRST page to avoid context limits
page_1_content = docs[0].page_content

# 3. Create the Prompt and Parser
prompt = PromptTemplate(
    template="Extract the main entities and key topics from the following page of a PDF:\n\n{text}",
    input_variables=["text"]
)
parser = StrOutputParser()

# 4. Build and invoke the chain
chain = prompt | model | parser

print(f"Total pages loaded: {len(docs)}")
print("\n--- Page 1 Metadata ---")
print(docs[0].metadata) # Notice it includes 'source' AND 'page' number

print("\n--- Chain Result (Page 1) ---")
result = chain.invoke({"text": page_1_content})
print(result)