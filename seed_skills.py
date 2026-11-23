"""Adds the starter skills catalog to the database.
Safe to run many times: skills that already exist are skipped.
Run with:  python seed_skills.py
"""
from app import create_app
from app.extensions import db
from app.models.skill import Skill

SKILLS = {
    "technical": [
        "Python", "Java", "JavaScript", "TypeScript", "C", "C++", "SQL",
        "HTML", "CSS", "React", "Node.js", "Flask", "Django", "REST APIs",
        "Data Structures", "Algorithms", "Object-Oriented Programming",
        "System Design", "Unit Testing", "Machine Learning", "Deep Learning",
        "Statistics", "Pandas", "NumPy", "Scikit-learn", "TensorFlow",
        "Data Visualization",
    ],
    "tool": [
        "Git", "GitHub", "Docker", "MySQL", "PostgreSQL", "MongoDB", "Linux",
        "Postman", "Excel", "Power BI", "Tableau", "AWS", "Jupyter Notebook",
        "VS Code",
    ],
    "soft": [
        "Communication", "Teamwork", "Problem Solving", "Leadership",
        "Time Management", "Critical Thinking", "Adaptability",
    ],
}

app = create_app()

with app.app_context():
    existing = {s.name.lower() for s in Skill.query.all()}
    added = 0
    for category, names in SKILLS.items():
        for name in names:
            if name.lower() not in existing:
                db.session.add(Skill(name=name, category=category))
                added += 1
    db.session.commit()
    total = Skill.query.count()
    print(f"Added {added} new skills. Total skills in database: {total}")