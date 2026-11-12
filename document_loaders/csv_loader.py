from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="sample.csv")


docs = loader.load()


print(f"Total rows loaded (excluding header): {len(docs)}\n")

# Loop through the first two rows to see the raw extracted format
for i, doc in enumerate(docs[:2]):
    print(f"--- Row {i + 1} Metadata ---")
    print(doc.metadata) 
    
    print(f"--- Row {i + 1} Page Content ---")
    print(doc.page_content)
    print("=" * 40)