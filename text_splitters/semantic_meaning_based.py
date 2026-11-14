from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings

raw_text = """
Retrieval-Augmented Generation enhances large language models. Base LLMs have knowledge cutoffs and hallucinate.
Python is a popular programming language for AI engineering. It is widely used for building backend servers and data pipelines.
"""

text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="percentile",
    breakpoint_threshold_amount=90
)

docs = text_splitter.create_documents([raw_text])

for i, doc in enumerate(docs):
    print(f"--- Chunk {i + 1} ---")
    print(doc.page_content)