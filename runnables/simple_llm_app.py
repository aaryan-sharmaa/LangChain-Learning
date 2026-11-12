from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

# Create Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# Get dynamic input
topic = input("Enter a topic: ")

# Format the prompt manually
formatted_prompt = prompt.format(topic=topic)

# Call the model directly
response = model.invoke(formatted_prompt)

# Print output
print("\nGenerated Blog Title:")
print(response.content) 