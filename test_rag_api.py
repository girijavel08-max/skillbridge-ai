
import requests
from getpass import getpass

BASE_URL = "http://127.0.0.1:5000/api"

email = input("Enter your registered email: ").strip()
password = getpass("Enter your password: ")

try:
    # Step 1: Login
    login = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "email": email,
            "password": password
        },
        timeout=20
    )

    if login.status_code != 200:
        print("LOGIN FAILED:", login.status_code, login.text)
        raise SystemExit

    token = login.json()["token"]

    headers = {
        "Authorization": f"Bearer {token}"
    }

    print("\nLOGIN SUCCESSFUL!")

    # Step 2: Ask RAG question
    question = "What skills are required for a Full Stack Developer?"

    response = requests.post(
        f"{BASE_URL}/rag/ask",
        headers=headers,
        json={"question": question},
        timeout=90
    )

    print("\nRAG API STATUS:", response.status_code)

    result = response.json()

    if response.status_code == 200:
        print("\nQUESTION:")
        print(result["data"]["question"])

        print("\nAI ANSWER:")
        print(result["data"]["answer"])

        print("\nRETRIEVED SOURCES:")
        for source in result["data"]["sources"]:
            print(source)

        print("\nSUCCESS: RAG API WORKING!")

    else:
        print("\nRAG API FAILED:")
        print(result)

except requests.exceptions.RequestException as error:
    print("Connection error:", error)
