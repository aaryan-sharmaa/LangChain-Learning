from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import RetrievalQA
from dotenv import load_dotenv
import os

load_dotenv()

# Load the document
loader = TextLoader("docs.txt", encoding="utf-8")
documents = loader.load()

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = text_splitter.split_documents(documents)

# Create embeddings and store in FAISS
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=os.getenv("OPENAI_API_KEY")
)

vectorstore = FAISS.from_documents(docs, embeddings)

# Create retriever
retriever = vectorstore.as_retriever()

# Initialize ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# Create RetrievalQA Chain
qa_chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

# Ask a question
query = input("Enter your question: ")

# Invoke the chain
response = qa_chain.invoke({"query": query})

# Print answer
print("\nANSWER:\n")
print(response["result"])

# Print source documents
print("\nSOURCE DOCUMENTS:\n")
for doc in response["source_documents"]:
    print(doc.page_content)