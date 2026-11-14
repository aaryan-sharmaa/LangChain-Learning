from langchain_text_splitters import CharacterTextSplitter

# Raw sample text simulating a long document
raw_text = """
Retrieval-Augmented Generation (RAG) is a technique that enhances large language models.
Base LLMs have a knowledge cutoff and are prone to hallucinations.
RAG solves this by injecting domain-specific context into the prompt.
By providing exact data, models generate accurate answers without expensive retraining.
"""

# Initialize the Character Text Splitter
text_splitter = CharacterTextSplitter(
    separator="\n",          # Split only on newlines
    chunk_size=100,          # Maximum size of each chunk (in characters)
    chunk_overlap=0          # No overlap between chunks
)

# Split the text
chunks = text_splitter.split_text(raw_text)

print(f"Total chunks created: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i + 1} ({len(chunk)} chars) ---")
    print(chunk.strip())