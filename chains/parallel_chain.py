from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv
import os

load_dotenv()

# Create ChatModel
model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0
)

parser = StrOutputParser()

# Prompt 1: Generate notes
prompt1 = PromptTemplate.from_template(
    "Generate short and simple notes from the following text:\n{text}"
)

# Prompt 2: Generate quiz questions
prompt2 = PromptTemplate.from_template(
    "Generate 5 short questions and answers from the following text:\n{text}"
)

# Prompt 3: Merge notes and quiz
prompt3 = PromptTemplate.from_template(
    "Merge the following notes and quiz into a single document.\n\n"
    "Notes:\n{notes}\n\nQuiz:\n{quiz}"
)

# Run both prompts in parallel
parallel_chain = RunnableParallel({
    "notes": prompt1 | model | parser,
    "quiz": prompt2 | model | parser
})

# Combine parallel outputs
chain = parallel_chain | prompt3 | model | parser

# Dynamic input
text = input("Enter your text: ")

result = chain.invoke({"text": text})

print("\nFINAL DOCUMENT:\n")
print(result)

# Print ASCII chain graph
print("\nChain Graph:")
chain.get_graph().print_ascii()