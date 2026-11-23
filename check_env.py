import os
from dotenv import load_dotenv

import flask
import flask_cors

load_dotenv()

print("Python packages: OK")
print("Flask version:", flask.__version__)
print()

for key in ["SECRET_KEY", "JWT_SECRET_KEY", "DB_HOST", "DB_PORT", "DB_USER", "DB_NAME"]:
    print(f"{key:16} ->", "set" if os.getenv(key) else "MISSING")

print(f"{'DB_PASSWORD':16} ->", "set" if os.getenv("DB_PASSWORD") else "MISSING")
print(f"{'NEXUS_API_KEY':16} ->", "set" if os.getenv("NEXUS_API_KEY") else "not set yet (expected until Step 9)")
