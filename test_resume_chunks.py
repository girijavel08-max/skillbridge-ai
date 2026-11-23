from app import create_app
from app.services.resume_retrieval import get_active_resume, chunk_resume_text

app = create_app()

with app.app_context():
    resume = get_active_resume(2)
    chunks = chunk_resume_text(resume.extracted_text, resume.id)
    print("Total chunks:", len(chunks))
    for c in chunks:
        print(f"\n{c['chunk_id']} | {c['heading']} | {len(c['text'].split())} words")
        print("   ", c["text"])