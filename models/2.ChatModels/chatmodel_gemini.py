import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    
    # max_output_tokens=10,
    
    # temperature=0,
)

response = model.invoke("Explain LangChain in two sentences.")
if isinstance(response.content, str):
    output = response.content
else:
    output = "".join(
        block.get("text", "")
        for block in response.content
        if isinstance(block, dict) and block.get("type") == "text"
    )

print(output)

# Token usage
usage = response.usage_metadata

print("\nToken Usage:")
print(f"Input tokens:  {usage['input_tokens']}")
print(f"Output tokens: {usage['output_tokens']}")
print(f"Total tokens:  {usage['total_tokens']}")