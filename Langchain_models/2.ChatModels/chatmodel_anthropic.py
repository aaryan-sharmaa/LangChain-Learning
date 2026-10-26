
import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(
    model="claude-sonnet-4-5-20250929",
    api_key=os.getenv("ANTHROPIC_API_KEY"),

    # Generation
    temperature=0.7,
    max_tokens=300,
    # top_p=0.9,
    # top_k=40,

    # # Reliability
    # timeout=30,
    # max_retries=2,
)

response = model.invoke("Explain LangChain in two sentences.")

print(response.content)
print("\nToken usage:", response.usage_metadata)
print("\nMetadata:", response.response_metadata)
