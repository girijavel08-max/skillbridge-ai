
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("NEXUS_API_KEY")

if not api_key:
    print("ERROR: Nexus API key not found.")
else:
    client = OpenAI(
        api_key=api_key,
        base_url="https://nexusapi.navigatelabs.ai"
    )

    try:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=["SkillBridge AI helps students improve their job readiness."]
        )

        print("SUCCESS: Embedding generated!")
        print("Embedding dimensions:", len(response.data[0].embedding))

    except Exception as error:
        print("Embedding test failed:")
        print(type(error).__name__, str(error))
