from app import create_app
from app.services.rag_service import ask_personalized_question

app = create_app()

with app.app_context():
    r = ask_personalized_question(2, "Which of my projects use React?")
    print(r["answer"])