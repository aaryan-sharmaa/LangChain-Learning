from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

# Initialize the chat model
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    max_output_tokens=100
)

# Create conversation messages
messages = [
    SystemMessage(content="You are a helpful AI tutor."),
    HumanMessage(content="What is machine learning?"),
    AIMessage(content="Machine learning allows computers to learn from data."),
    HumanMessage(content="Give me an example.")
]

# Display the messages
print("Conversation History:\n")

for message in messages:
    print(f"{message.type}: {message.content}\n")

# Send the conversation to the model
response = model.invoke(messages)

# Display the AI's response
print("AI Response:")
print(response.content)