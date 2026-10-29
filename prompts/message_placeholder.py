from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

with open("chat_history.txt", "r", encoding="utf-8") as file:
    for line in file:
        role, content = line.strip().split(":", 1)

        if role == "Human":
            chat_history.append(HumanMessage(content=content.strip()))
        elif role == "AI":
            chat_history.append(AIMessage(content=content.strip()))

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support chatbot."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

messages = template.format_messages(
    chat_history=chat_history,
    query="How long will my refund take?"
)

for message in messages:
    print(f"{message.type}: {message.content}")