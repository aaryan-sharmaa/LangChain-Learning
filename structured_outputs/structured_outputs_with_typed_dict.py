from typing import Optional
from typing_extensions import TypedDict, Annotated, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

class ReviewSummary(TypedDict):
    
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    key_themes: Annotated[list[str], "Write down all the key themes discussed in a review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative", "mixed", "neutral"], "Return sentiment of the review negative, positive, mixed or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]


structured_model = model.with_structured_output(ReviewSummary)

review = """
The laptop has excellent performance and a great display.
The battery lasts only four hours, and the fan gets noisy.
It's good for coding, but the battery life could be better.
"""

response = structured_model.invoke(
    f"Summarize this review and identify its sentiment: {review}"
)

print(response)