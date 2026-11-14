from langchain_text_splitters import RecursiveCharacterTextSplitter

raw_text = """
Retrieval-Augmented Generation (RAG) is a technique that enhances large language models (LLMs) by connecting them to external knowledge bases. While base LLMs are powerful, their knowledge is frozen in time at the point of their training, and they are prone to hallucinating facts when asked about proprietary or recent information.

To solve this, RAG introduces a retrieval step before generation. When a user asks a question, the system searches a vector database containing domain-specific documents to find the most relevant information. This retrieved context is then injected into the prompt alongside the user's original query. 

By providing the LLM with this exact, grounded context, the model can generate highly accurate and specific answers. This approach not only reduces hallucinations but also allows developers to build AI applications that securely query private enterprise data without needing to expensively retrain or fine-tune the underlying model.
"""

# Initialize the Recursive Splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,          # Target maximum characters per chunk
    chunk_overlap=20,        # Overlap characters to maintain context across boundaries
    separators=["\n\n", "\n", " ", ""] # Order of fallback separators (Paragraph -> Line -> Word -> Char)
)

# Split the text into string chunks
chunks = text_splitter.split_text(raw_text)

print(f"Total chunks created: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i + 1} ({len(chunk)} chars) ---")
    print(chunk)
    print("=" * 40)