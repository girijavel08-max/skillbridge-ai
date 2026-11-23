from app.services.vector_store import retrieve_relevant_chunks

queries = [
    "How do I containerize my application?",
    "What is a JWT token?",
    "How do I write SQL joins?",
    "What is the best pizza recipe?",
]

for query in queries:
    print("\nQUERY:", query)
    for r in retrieve_relevant_chunks(query, top_k=3):
        print(f"  {r['similarity']:.4f} | {r['chunk_id']} | {r['heading']}")