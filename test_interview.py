import requests
from getpass import getpass

BASE_URL = "http://127.0.0.1:5000/api"

email = input("Enter your registered email: ")
password = getpass("Enter your password: ")

try:
    login = requests.post(
        f"{BASE_URL}/login",
        json={"email": email, "password": password},
        timeout=20
    )

    if login.status_code != 200:
        print("LOGIN FAILED:", login.status_code, login.text)
        raise SystemExit

    token = login.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    print("\nLOGIN SUCCESSFUL!")

    start = requests.post(
        f"{BASE_URL}/interviews/start",
        headers=headers,
        timeout=20
    )

    if start.status_code != 201:
        print("INTERVIEW START FAILED:", start.text)
        raise SystemExit

    data = start.json()
    session_id = data["session_id"]
    questions = data["questions"]

    print("\nINTERVIEW STARTED. Session ID:", session_id)

    for index, question in enumerate(questions, start=1):
        print(f"\nQUESTION {index}: {question}")
        answer = input("Your answer: ").strip()

        result = requests.post(
            f"{BASE_URL}/interviews/{session_id}/answer",
            headers=headers,
            json={"question_no": index, "answer": answer},
            timeout=60
        )

        print("HTTP Status:", result.status_code)
        print("AI Evaluation:", result.text)

        if result.status_code != 201:
            print("Answer submission failed. Stopping test.")
            raise SystemExit

    finish = requests.post(
        f"{BASE_URL}/interviews/{session_id}/finish",
        headers=headers,
        timeout=20
    )

    print("\nFINAL INTERVIEW RESULT:")
    print("HTTP Status:", finish.status_code)
    print(finish.text)

except requests.RequestException as error:
    print("CONNECTION ERROR:", error)
