from app import create_app
from app.models.user import User
from app.models.resume import Resume
from app.services.resume_retrieval import retrieve_resume_evidence

app = create_app()

QUERY = "Which projects did I build using React or JavaScript?"

with app.app_context():
    for user in User.query.all():
        result = retrieve_resume_evidence(user.id, QUERY, top_k=3)
        print(f"\n=== User id {user.id} ===")

        if not result["has_resume"]:
            print("No resume found (handled gracefully).")
            continue

        resume = Resume.query.get(result["resume_id"])
        print("Resume id:", result["resume_id"], "| owner id:", resume.user_id)

        for c in result["chunks"]:
            print(f"  {c['similarity']:.4f} | {c['chunk_id']} | {c['heading']}")
            print("     ", c["text"][:120].replace("\n", " "))

        # ISOLATION CHECK
        ok = resume.user_id == user.id and all(
            c["chunk_id"].startswith(f"resume-{resume.id}#") for c in result["chunks"]
        )
        print("ISOLATION OK:", ok)

    print("\n=== Non-existing user (id 99999) ===")
    print(retrieve_resume_evidence(99999, QUERY))