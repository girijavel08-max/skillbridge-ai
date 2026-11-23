import requests
from getpass import getpass

BASE_URL = "http://127.0.0.1:5000/api"

email = input("Enter your registered email: ").strip()
password = getpass("Enter your password: ")

login = requests.post(f"{BASE_URL}/auth/login",
                      json={"email": email, "password": password}, timeout=20)
if login.status_code != 200:
    print("LOGIN FAILED:", login.status_code, login.text)
    raise SystemExit

headers = {"Authorization": f"Bearer {login.json()['token']}"}
print("LOGIN OK")

# 1. Full career analysis
r = requests.get(f"{BASE_URL}/career/analysis", headers=headers, timeout=90)
print("\nANALYSIS STATUS:", r.status_code)
body = r.json()

if r.status_code == 200:
    data = body["data"]
    print("Role:", data["role"], "| Summary:", data["summary"])
    for s in data["skills"][:5]:
        print(f"  {s['priority_score']:>6} {s['priority_level']:<7} {s['skill']:<11} {s['state']}")
        for k in s.get("kb_sources", []):
            print("       KB:", k["chunk_id"], k["similarity"])
else:
    print(body)

# 2. Retrieval demo: two different queries
for q in ["How do I use Docker containers?", "Tell me about React projects"]:
    d = requests.post(f"{BASE_URL}/career/retrieval-demo", headers=headers,
                      json={"query": q}, timeout=60).json()["data"]
    print("\nQUERY:", q)
    print("  KB    :", [(c["chunk_id"], c["similarity"]) for c in d["knowledge_base"]])
    print("  RESUME:", [(c["chunk_id"], c["similarity"]) for c in d["resume"]])

# 3. No token must be rejected
r2 = requests.get(f"{BASE_URL}/career/analysis", timeout=20)
print("\nNO TOKEN STATUS (expect 401):", r2.status_code)