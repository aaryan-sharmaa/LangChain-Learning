import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    max_output_tokens=100,
)

history = []

while True:
    prompt = input("You: ")
    if prompt.lower() == "exit":
        break

    history.append(HumanMessage(content=prompt))
    response = model.invoke(history)
    print("Gemini:", response.content)
    history.append(AIMessage(content=response.content))