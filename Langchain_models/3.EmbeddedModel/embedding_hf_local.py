
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
)

vector = embeddings.embed_query("What is machine learning?")

print("Dimensions:", len(vector))  # 384
print(vector[:5])
