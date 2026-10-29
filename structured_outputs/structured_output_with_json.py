import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

with open("review_schema.json", "r") as file:
    review_schema = json.load(file)

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

structured_model = model.with_structured_output(
    review_schema,
    method="json_schema",
    strict=True
)

review = "Great performance, but poor battery life."

response = structured_model.invoke(
    f"Summarize this product review: {review}"
)

print(response)