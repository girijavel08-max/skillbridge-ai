from app.services.document_loader import load_documents, load_and_split_documents

documents = load_documents()
chunks = load_and_split_documents()

print("Documents found:", len(documents))
print("Chunks created:", len(chunks))

for chunk in chunks:
    print("\nSource:", chunk["source"])
    print("Chunk ID:", chunk["chunk_id"])
    print("Content:", chunk["text"][:150], "...")