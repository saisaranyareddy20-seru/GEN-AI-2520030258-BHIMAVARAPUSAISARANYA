# Google Gemini AI Model Integration

## Project Overview

This project is about connecting Google Gemini AI with Python using the Gemini API. It allows the Python program to send a question to the AI model and display the response in the terminal.

The program uses different Gemini models to generate responses. If one model is not available, it automatically tries another model. This helps the application continue working even when a particular model cannot be accessed.

## Objectives

- To learn how to connect Python with Google Gemini AI.
- To understand the basic working of Generative AI.
- To generate answers using the Gemini API.
- To learn how to handle API errors and unavailable models.

## Technologies Used

- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- Visual Studio Code

## Project Structure

```text
Gemini-AI-Project/
│
├── main.py
├── .env
├── .gitignore
└── README.md
```

## Features

- Connects a Python program to Google Gemini AI.
- Uses an API key to access the Gemini service.
- Keeps the API key in an environment file.
- Tries different Gemini models if one is unavailable.
- Generates answers based on the given prompt.
- Displays the AI-generated response in the terminal.

## Installation

First, install the required Python packages using the following command:

```bash
pip install google-genai python-dotenv
```

## Configuration

Create a file named `.env` in your project folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

This file is used to store the API key securely.

## How to Run the Project

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Install the required packages.
4. Make sure the API key is configured in the `.env` file.
5. Run the following command:

```bash
python main.py
```

## Expected Output

When the program runs, it connects to the Gemini API and tries the available models. Once a model responds successfully, the answer is displayed in the terminal.

**Example Prompt:**

"What is Artificial Intelligence? Explain in simple words."

The Gemini model generates an answer based on the given question.

## Security

- The API key is stored in the `.env` file.
- The `.env` file should not be uploaded to GitHub.
- The `.env` file is added to `.gitignore` to prevent accidental uploads.
- API keys should always be kept private.

## Future Enhancements

- Allow users to enter their own questions.
- Add a simple web interface for better interaction.
- Include more features of Google Gemini AI.
- Improve the program to answer different types of questions.

## Conclusion

This project helped us understand how to connect Python with Google Gemini AI and generate responses using the Gemini API. It also gave us practical knowledge of API integration, environment variables, and error handling. This project can be further improved by adding more AI features and a user-friendly interface.
