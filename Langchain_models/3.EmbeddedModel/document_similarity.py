
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    dimensions=32,
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

query = "How do computers learn from data?"

docs = [
    "Machine learning helps computers learn from data.",
    "Deep learning uses neural networks.",
    "Pizza is my favourite food.",
]

query_vector = embeddings.embed_query(query)
doc_vectors = embeddings.embed_documents(docs)



scores = cosine_similarity([query_vector], doc_vectors)[0]

ranked_docs = sorted(
    zip(docs, scores),
    key=lambda x: x[1],
    reverse=True
)

print("\nMost relevant document:")
print(ranked_docs[0][0])
print(f"Similarity: {ranked_docs[0][1]:.3f}")

print("\nAll document scores:")
for doc, score in ranked_docs:
    print(f"{score:.3f} | {doc}")



# scores = cosine_similarity([query_vector], doc_vectors)[0]

# for doc, score in sorted(zip(docs, scores), key=lambda x: x[1], reverse=True):
#     print(f"{score:.3f} | {doc}")

