# Multi-Provider LLM Integration Using Python

## Project Overview

This project is developed using Python to work with two AI platforms: Google Gemini and Ollama.

The program allows users to choose either Gemini or Ollama and enter a question. Based on the selected option, the AI model generates an answer and displays it on the screen.

If a Gemini model is temporarily unavailable, the program tries again and then checks other available models. Ollama is used to run an AI model locally on the computer.

## Objectives

- To learn how to connect Python with AI models.
- To understand how Gemini and Ollama work.
- To allow users to choose between two AI providers.
- To get answers for different questions using AI.
- To handle errors when a model is not working.
- To test whether the program is working correctly.

## Technologies Used

- Python
- Google Gemini API
- Ollama
- Llama 3.2
- Google Gen AI SDK
- Requests
- python-dotenv
- Pytest
- Visual Studio Code

## Project Structure

```text
week2/
│
├── main.py
├── llm_client.py
├── test_client.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Features

- Users can select Gemini or Ollama.
- Users can enter their own questions.
- Gemini generates answers using its API.
- Ollama generates answers using a local AI model.
- The program tries another Gemini model if the first one is unavailable.
- It displays an error message if the connection fails.
- A separate test file is included to check the program.

## Installation

First, install the required Python packages by running this command:

```bash
pip install -r requirements.txt
```

## Configuration

For using Gemini, create a `.env` file and add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

For using Ollama, install Ollama and download the required model:

```bash
ollama pull llama3.2
```

## How to Run

Open the project folder in Visual Studio Code and run:

```bash
python main.py
```

The program will ask you to select a provider:

```text
Choose provider (gemini/ollama):
```

Enter either `gemini` or `ollama`.

Next, enter your question:

```text
Enter your question: Explain Artificial Intelligence in simple words.
```

The selected AI model will process the question and display the answer in the terminal.

## Testing

The project also contains a file named `test_client.py` to check whether the LLM client is working properly.

Run the following command:

```bash
python -m pytest -v
```

The test was executed successfully, and the result was **1 passed**.

## Security

- The Gemini API key is stored in the `.env` file.
- The `.env` file is added to `.gitignore`.
- API keys should not be shared publicly.
- The `.env` file should not be uploaded to GitHub.

## Future Enhancements

- Add more AI platforms to the project.
- Create a simple website for users.
- Allow users to ask multiple questions.
- Improve the way errors are handled.
- Add more test cases.

## Conclusion

Through this project, we learned how to connect Python with Gemini and Ollama. We also understood how to select different AI models, enter questions, and get answers from them. This project gave us practical experience in working with AI models, Python packages, and testing. In the future, we can improve it by adding more AI platforms and new features.
