from app.services.rag_service import ask_rag_question

question = "What skills should I learn to become a Full Stack Developer?"

try:
    result = ask_rag_question(question)

    print("\nQUESTION:")
    print(result["question"])

    print("\nAI GENERATED ANSWER:")
    print(result["answer"])

    print("\nRETRIEVED SOURCES:")

    for source in result["sources"]:
        print(
            source["source"],
            "| Chunk:", source["chunk_id"],
            "| Similarity:", source["similarity"]
        )

except Exception as error:
    print("RAG test failed:")
    print(type(error).__name__, str(error))