
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimensions=32,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

# Embed a single query
query_vector = embeddings.embed_query(
    "What is machine learning?"
)

print("Query embedding:")
print(query_vector[:10])
print("Vector dimensions:", len(query_vector))

# Embed multiple documents
documents = [
    "Machine learning enables systems to learn from data.",
    "Deep learning uses multi-layer neural networks.",
    "Delhi is the capital of India.",
]

document_vectors = embeddings.embed_documents(documents)

print("\nNumber of document vectors:", len(document_vectors))
print("Dimensions per vector:", len(document_vectors[0]))
