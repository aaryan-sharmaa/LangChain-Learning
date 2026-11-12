from typing import Literal
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnablePassthrough, RunnableLambda
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

# Pydantic schema
class Sentiment(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Sentiment of the customer feedback"
    )

parser = PydanticOutputParser(pydantic_object=Sentiment)
str_parser = StrOutputParser()

# Prompt 1: Classify sentiment
prompt1 = PromptTemplate(
    template="Classify this feedback as positive or negative:\n{feedback}\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

classifier_chain = prompt1 | model | parser

# Prompt 2: Positive response
prompt2 = PromptTemplate.from_template(
    "Write a friendly response to this positive feedback: {feedback}"
)

# Prompt 3: Negative response
prompt3 = PromptTemplate.from_template(
    "Write an empathetic response to this negative feedback: {feedback}"
)

# Conditional branching
branch_chain = RunnableBranch(
    (
        lambda x: x["sentiment"].sentiment == "positive",
        prompt2 | model | str_parser
    ),
    (
        lambda x: x["sentiment"].sentiment == "negative",
        prompt3 | model | str_parser
    ),
    RunnableLambda(lambda x: "Could not determine sentiment")
)

# Preserve feedback and add the classified sentiment
chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | branch_chain
)

# Run chain
feedback = input("Enter customer feedback: ")
result = chain.invoke({"feedback": feedback})

print("\nResponse:", result)