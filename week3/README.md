LLM Client with Usage Tracking

This project sends your question to an AI model and prints the answer. It also saves the usage details (tokens, time, cost) in MongoDB.

Providers
Gemini: Google's online AI. If one model is not working, it tries the next one.
Ollama: an AI that runs on your own computer.
Files
main.py: starts the app
llm_client.py: talks to Gemini or Ollama and retries if there is an error
usage_logger.py: saves usage details in MongoDB
test_client.py: a simple test
requirements.txt: list of packages to install
Setup

Step 1: Install the packages

pip install -r requirements.txt

Step 2: Create a file named .env and add this:

GEMINI_API_KEY=your_gemini_api_key
MONGODB_URI=your_mongodb_connection_string
GEMINI_INPUT_PRICE_PER_MILLION=0
GEMINI_OUTPUT_PRICE_PER_MILLION=0

The two price lines are for the cost estimate. Put the real prices there, or leave them as 0.

Step 3: Only if you use Ollama, run these:

ollama pull llama3.2
ollama serve

Run

python main.py

Choose gemini or ollama, then type your question. The answer will be shown on the screen.

What Is Saved in MongoDB
provider and model name
input, output and total tokens
time taken
estimated cost
success or failed status
date and time

The data goes to the database llm_monitoring, in the collection api_usage.

Run the Test

python -m unittest test_client.py

Notes
If a request fails for a short time, the app tries again up to 3 times.
Do not share your .env file with anyone.
