from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI tutor who explains {topic} simply."),
    ("human", "Explain {concept} with a real-world example.")
])

messages = chat_template.format_messages(
    topic="Machine Learning",
    concept="Overfitting"
)

for message in messages:
    print(f"{message.type}: {message.content}\n")