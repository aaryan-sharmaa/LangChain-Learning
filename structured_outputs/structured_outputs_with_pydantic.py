from pydantic import BaseModel, Field
from typing import Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Create ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# Define Pydantic schema
class ReviewSummary(BaseModel):
    summary: str = Field(description="Brief summary of the review")
    sentiment: Literal["positive", "negative", "mixed", "neutral"]
    pros: list[str] = Field(description="Positive points mentioned")
    cons: list[str] = Field(description="Negative points mentioned")
    rating: int = Field(description="Estimated rating out of 5")
    recommendation: str = Field(description="Final recommendation")

# Create structured model
structured_model = model.with_structured_output(ReviewSummary)

# Sample review
review = """
The laptop is fast and has an excellent display.
However, battery life is poor and the fan gets noisy.
It's great for coding, but not ideal for travel.
"""

# Generate structured summary
response = structured_model.invoke(
    f"Analyze this product review:\n{review}"
)

print(response.model_dump())