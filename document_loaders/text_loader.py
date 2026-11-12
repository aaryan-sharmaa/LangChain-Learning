from langchain_community.document_loaders import TextLoader
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

# 2. Load the document (The new LC#12 concept)
# Make sure to create a 'sample.txt' file in your directory before running this
loader = TextLoader("sample.txt", encoding="utf-8")
docs = loader.load()

# The loader returns a list of Document objects. 
# Since it's one file, we grab the first item [0] and extract its text content.
document_content = docs[0].page_content

# 3. Create the Prompt and Parser (Concepts you already know)
prompt = PromptTemplate(
    template="Summarize the following text in exactly 3 bullet points:\n\n{text}",
    input_variables=["text"]
)
parser = StrOutputParser()

# 4. Build and invoke the chain
chain = prompt | model | parser

print("--- Document Metadata ---")
print(docs[0].metadata) # Shows source file info

print("\n--- Chain Result ---")
result = chain.invoke({"text": document_content})
print(result)