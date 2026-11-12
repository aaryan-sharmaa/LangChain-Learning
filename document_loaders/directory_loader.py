from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader
import os

# 1. Setup the Directory Loader
# We point it to the 'books' folder, tell it to only look for .txt files, 
# and explicitly tell it to use the TextLoader we used earlier.
loader = DirectoryLoader(
    path="./books",
    glob="*.pdf",
    loader_cls=PyPDFLoader,
    show_progress=True
)

# 2. Load all matching documents in the folder
docs = loader.load()

print(f"Total books loaded: {len(docs)}\n")

# 3. Inspect what LangChain extracted
for i, doc in enumerate(docs):
    print(f"--- Book {i+1} ---")
    print(f"Source: {doc.metadata['source']}")
    # Printing just the first 100 characters so we don't flood the terminal
    print(f"Preview: {doc.page_content[:100]}...\n")