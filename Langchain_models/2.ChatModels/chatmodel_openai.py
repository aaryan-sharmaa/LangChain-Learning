
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=os.getenv("OPENAI_API_KEY"),

    # Generation
    temperature=0.7,
    max_tokens=300,
    # top_p=1,

    # # Repetition control
    # frequency_penalty=0.0,
    # presence_penalty=0.0,

    # # Reliability
    # timeout=30,
    # max_retries=2,
)

response = model.invoke("Explain LangChain in two sentences.")

print(response.content)
print("\nToken usage:", response.usage_metadata)
print("\nMetadata:", response.response_metadata)
