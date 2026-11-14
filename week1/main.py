
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: API key not found in .env file!")
    exit()

# Initialize Gemini client
client = genai.Client(api_key=API_KEY)

# Models available in your API model list
models = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash",
    "gemini-3.5-flash-lite"
]

# Input prompt
prompt = "What is Artificial Intelligence? Explain in simple words."

print("\nConnecting to Gemini AI...")

# Try available models one by one
for model in models:
    try:
        print(f"\nTrying model: {model}")

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        print("\n" + "=" * 50)
        print("             GEMINI AI RESPONSE")
        print("=" * 50)

        print(response.text)

        print("\n" + "=" * 50)
        print("SUCCESS! Response generated.")
        print("Model used:", model)
        print("=" * 50)

        break

    except Exception as error:
        print("Model failed:", error)

else:
    print("\nAll models are currently unavailable.")
    print("Please check your API quota and try again later.")
