# Week 6 – Generative AI Practical

## Project Title
Baseline Evaluation of Llama 3.2 using Ollama.

## 1. Introduction
This project is used to test the performance of the Llama 3.2 AI model.

We give questions to the AI model and check whether its answers contain the expected keywords.

## 2. Tools Used
- Python
- VS Code
- Ollama
- Llama 3.2

## 3. Project Files
- **main.py** – Contains the Python program.
- **golden_set.json** – Contains questions and expected answers.
- **requirements.txt** – Contains the required Python library.
- **baseline_results.csv** – Stores the final results.
- **README.md** – Contains project information.

## 4. Installation

Download the Llama 3.2 model:

powershell
ollama pull llama3.2


Install the required library:

powershell
python -m pip install -r requirements.txt


## 5. How to Run

Open the project in VS Code.

Run this command in the terminal:

powershell
python main.py


## 6. How It Works

1. Loads questions from the JSON file.
2. Sends questions to the Llama 3.2 model.
3. Gets answers from the AI model.
4. Checks the answers using keywords.
5. Calculates the score.
6. Saves the results in a CSV file.

## 7. Output

The program creates a file called:

**baseline_results.csv**

It contains the questions, AI answers, scores and results.

- PASS – Score is 60% or above.
- REVIEW – Score is below 60%.
- ERROR – An error occurs.

## 8. Conclusion

This project helps us understand how to test and evaluate an AI language model.

We used Llama 3.2 with Ollama and Python to generate answers and calculate scores.

The experiment is named Release v0.1.
