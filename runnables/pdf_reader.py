from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

# Load the document
loader = TextLoader("docs.txt", encoding="utf-8")
documents = loader.load()

# Split text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Convert text into embeddings and store in FAISS
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY")
)

vectorstore = FAISS.from_documents(docs, embeddings)

# Create retriever
retriever = vectorstore.as_retriever()

# Retrieve relevant documents
query = input("Enter your question: ")
retrieved_docs = retriever.invoke(query)

# Combine retrieved text
retrieved_text = "\n".join(
    [doc.page_content for doc in retrieved_docs]
)

# Initialize ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

# Pass retrieved text to ChatModel
prompt = f"""
Based on the following text, answer the question: {query}

{retrieved_text}
"""

answer = model.invoke(prompt)

# Print the answer
print("\nAnswer:")
print(answer.content)