from app.services.vector_store import retrieve_relevant_chunks

query = "What skills are required for a Full Stack Developer?"

try:
    results = retrieve_relevant_chunks(query, top_k=3)

    print("Query:", query)
    print("\nRetrieved Documents:", len(results))

    for result in results:
        print("\nSource:", result["source"])
        print("Chunk ID:", result["chunk_id"])
        print("Similarity:", round(result["similarity"], 4))
        print("Content:", result["text"][:250])

except Exception as error:
    print("Retrieval failed:")
    print(type(error).__name__, str(error))