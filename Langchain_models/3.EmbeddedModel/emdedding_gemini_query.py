
import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

vector = embeddings.embed_query("What is machine learning?")

print("Dimensions:", len(vector))
print("First 5 values:", vector[:5])
