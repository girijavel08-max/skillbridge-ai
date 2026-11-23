from app import create_app
from app.services.rag_service import ask_personalized_question

app = create_app()

QUESTIONS = [
    "Do I have Docker experience?",
    "Which of my projects use React?",
    "What is the best pizza recipe?",
]

with app.app_context():
    for uid in (2, 1):
        print(f"\n################ USER {uid} ################")
        for q in QUESTIONS:
            r = ask_personalized_question(uid, q)
            print("\nQ:", q)
            print("A:", r["answer"][:350])
            print("  KB    :", [(c["chunk_id"], c["similarity"]) for c in r["knowledge_base"]])
            print("  RESUME:", [(c["chunk_id"], c["similarity"]) for c in r["resume"]])