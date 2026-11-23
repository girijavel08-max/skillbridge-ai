from app import create_app
from app.services.evidence_engine import analyze_resume_evidence
from app.services.priority_engine import prioritize_skills

app = create_app()

with app.app_context():
    for uid in (2, 1):
        evidence = analyze_resume_evidence(uid, role_id=3)
        result = prioritize_skills(uid, evidence)
        print(f"\n===== USER {uid} =====")
        for s in result["skills"]:
            print(f"{s['priority_score']:>6} {s['priority_level']:<7} {s['skill']:<11} {s['state']}")
        print("\nExample:", result["skills"][0]["priority_explanation"])