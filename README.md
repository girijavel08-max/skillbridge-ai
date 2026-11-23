# SkillBridge AI

Evidence-based career readiness platform powered by multi-source RAG.

## What it does

A student uploads a resume and selects a target role. The system retrieves
evidence from the student's own resume, compares it with the role's required
skills, and produces explainable skill-gap priorities.

## Stack

- Frontend: React, Vite, JavaScript
- Backend: Python, Flask, Flask-JWT-Extended, SQLAlchemy, MySQL
- AI (Nexus API): `text-embedding-3-small` (embeddings), `nova-micro` (text generation)
- Retrieval: custom implementation. Chunking, embeddings, cosine similarity
  and top-k ranking are written in Python. A JSON file stores the knowledge-base
  vectors. No FAISS, ChromaDB or LangChain is used.

## RAG pipeline

1. Knowledge base: 5 curated documents in `backend/data/knowledge_base/`,
   split into heading-based chunks (one section = one chunk, 43 chunks) and
   embedded. Stored in `vector_index.json`.
2. Student resume: extracted PDF text is chunked by section and project,
   embedded on demand and cached in memory only, keyed by user and resume.
   Resumes are never written to the shared index.
3. A query is embedded and ranked by cosine similarity against each source
   separately. Chunks below a similarity threshold are discarded.
4. If nothing passes the threshold, the LLM is not called.
5. Retrieved chunks are passed to the LLM in labelled sections
   ([RESUME EVIDENCE], [KNOWLEDGE BASE]) and the answer returns source names,
   chunk IDs and similarity scores.

## Deterministic vs LLM parts

Deterministic (plain Python, no LLM):
- Resume chunking, retrieval, ranking, similarity thresholds
- Evidence classification: Evidence Found / Weak or Insufficient Evidence /
  No Evidence Found (retrieval + skill-name match + section context)
- Skill priority score:
  `importance x (0.50 x evidence gap + 0.35 x assessment gap + 0.15 x status gap) x 100`

LLM-generated:
- Natural-language answers in RAG Chat and "Ask about my resume"
- Mock interview questions and evaluation

A skill named in a resume is never marked verified. Only a passed quiz
removes the "needs practical validation" flag.

## Security

- All career endpoints require a JWT.
- The user ID comes from the token, never from the request body.
- Resume queries are filtered by user ID.
- API keys are read from `backend/.env` and are never sent to the frontend.

## Main files

- `backend/app/services/document_loader.py`: knowledge-base loading and chunking
- `backend/app/services/vector_store.py`: embeddings, cosine similarity, ranking
- `backend/app/services/resume_retrieval.py`: private per-user resume retrieval
- `backend/app/services/evidence_engine.py`: evidence classification
- `backend/app/services/priority_engine.py`: priority formula
- `backend/app/services/rag_service.py`: RAG generation
- `backend/app/routes/career.py`: `/api/career/*` endpoints
- `frontend/src/pages/CareerIntelligence.jsx`: analysis and Retrieval Evidence UI

## Run

Backend (from `backend/`, venv active): `python run.py`
Frontend (from `frontend/`): `npm run dev`

## Known limitations

- Detailed knowledge base and required-skill data exist for Full Stack Developer only.
- Skill aliases (for example MySQL for SQL) are a manual list.
- Evidence checks use skill-name matching, so it cannot judge code quality.
- JSON vector store suits a small knowledge base. For thousands of users,
  a vector database would replace it.