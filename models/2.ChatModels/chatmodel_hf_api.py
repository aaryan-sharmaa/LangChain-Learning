
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    max_new_tokens=200,
    do_sample=False,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Explain LangChain in two sentences.")
print(response.content)
