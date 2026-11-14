from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

# Sample document text containing Python code snippets and explanations
tech_document = """
# Utility Functions
Below are core helper functions for our pipeline.

def process_payload(data):
    # Clean and validate input records
    if not data:
        return None
    return [x.strip() for x in data if x]

class PipelineManager:
    def __init__(self, timeout=30):
        self.timeout = timeout

    def execute(self):
        print("Running pipeline...")
"""

# 1. Initialize the text splitter using Python language rules
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=150,    # Maximum characters per chunk
    chunk_overlap=0
)

# 2. Create document chunks
chunks = splitter.create_documents([tech_document])

# 3. Inspect the resulting chunks
print(f"Total chunks created: {len(chunks)}\n")
for i, chunk in enumerate(chunks):
    print(f"--- Chunk {i + 1} ({len(chunk.page_content)} chars) ---")
    print(chunk.page_content)
    print("=" * 40)