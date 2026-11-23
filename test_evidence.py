from app import create_app
from app.services.evidence_engine import analyze_resume_evidence

app = create_app()

with app.app_context():
    for uid in (2, 1, 99999):
        result = analyze_resume_evidence(uid, role_id=3)
        print(f"\n===== USER {uid} =====")

        if not result.get("has_resume"):
            print(result["message"])
            continue

        print("Role:", result["role"], "| Summary:", result["summary"])

        for s in result["skills"]:
            print(f"\n{s['skill']:<11} {s['state']:<30} strength={s['evidence_strength']} sim={s['similarity']} chunk={s['chunk_id']}")
            print("   why:", s["reason"])
            if s["evidence_text"]:
                print("   evidence:", s["evidence_text"])