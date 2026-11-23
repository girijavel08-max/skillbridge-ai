from app import create_app
from app.models.user import JobRole, User
from app.models.skill import RoleRequiredSkill
from app.models.resume import Resume

app = create_app()

with app.app_context():
    print("Users:", User.query.count(), "| Resumes:", Resume.query.count())

    for role in JobRole.query.all():
        reqs = RoleRequiredSkill.query.filter_by(role_id=role.id).all()
        print(f"\n[{role.id}] {role.name} -> {len(reqs)} required skills")
        for r in sorted(reqs, key=lambda x: -float(x.importance)):
            print("   ", r.skill.name, "| importance:", float(r.importance))