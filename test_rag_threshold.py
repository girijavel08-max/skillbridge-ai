from app.services.rag_service import ask_rag_question

for q in ["How do I containerize my application?", "What is the best pizza recipe?"]:
    r = ask_rag_question(q)
    print("\nQUESTION:", q)
    print("Retrieved:", r["retrieved_count"], "| Threshold:", r["threshold"])
    print("Answer:", r["answer"][:200])
    for s in r["sources"]:
        print("  ", s["similarity"], s["chunk_id"], "|", s["heading"])