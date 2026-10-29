
import os
from dotenv import load_dotenv
from huggingface_hub import login
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
login(token=token)

llm = HuggingFacePipeline.from_model_id(
    model_id="openai-community/gpt2",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "do_sample": False,
    },
)

chat_model = ChatHuggingFace(llm=llm)

response = chat_model.invoke("Explain LangChain in two sentences.")
print(response.content)
