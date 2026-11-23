"""Creates backend/.env with random secret keys and your MySQL password.
Run once:  python setup_env.py
"""
import os
import secrets
from getpass import getpass

ENV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")

if os.path.exists(ENV_PATH):
    print(".env already exists. Delete it first if you want to create it again.")
    raise SystemExit(0)

print("Enter your MySQL root password (typing is hidden, press Enter when done).")
password = getpass("MySQL password: ")
escaped = password.replace("\\", "\\\\").replace('"', '\\"')

content = f'''# Flask security keys (auto-generated)
SECRET_KEY={secrets.token_hex(32)}
JWT_SECRET_KEY={secrets.token_hex(32)}

# MySQL database
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD="{escaped}"
DB_NAME=skillbridge_db

# Nexus API (filled in during Step 9, after checking the docs)
NEXUS_API_KEY=
'''

with open(ENV_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print(".env created successfully. Never share or upload this file.")
