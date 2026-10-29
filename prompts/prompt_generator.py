from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Explain the research paper: {paper_input}

Explanation Style: {style_input}
Explanation Length: {length_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present.
   - Explain concepts with intuitive examples.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

Ensure the explanation is clear and accurate.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save("template.json")