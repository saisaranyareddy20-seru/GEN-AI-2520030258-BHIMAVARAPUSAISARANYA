# Week 7 – GPT-2 Language Model and Probability Analysis

## Project Overview

This project focuses on loading and using a small open-source language model, GPT-2, for text generation and probability analysis.

The project uses PyTorch and Hugging Face Transformers to load the pretrained GPT-2 model, process text inputs, and generate language-model outputs.

## Objectives

- Load a pretrained GPT-2 language model.
- Use Hugging Face Transformers for tokenization.
- Implement language generation using PyTorch.
- Explore token-level probability analysis.
- Store probability-related results in a CSV file.
- Understand how pretrained language models generate text.

## Technologies Used

- **Programming Language:** Python
- **Deep Learning Framework:** PyTorch
- **NLP Library:** Hugging Face Transformers
- **Model:** GPT-2
- **Data Storage:** CSV
- **IDE:** Visual Studio Code

## Project Structure

```text
week7/
│
├── main.py
├── requirements
└── week7_probability_results.csv
```

### File Description

| File | Description |
|---|---|
| `main.py` | Main Python program for loading and using GPT-2 |
| `requirements` | Required Python packages |
| `week7_probability_results.csv` | CSV file for probability-related results |

## Model Information

The project uses the pretrained GPT-2 model.

**Model Name:**
```python
MODEL_NAME = "openai-community/gpt2"
```

GPT-2 is an autoregressive language model that predicts the next token based on previously provided tokens.

## Installation and Setup

### 1. Clone or download the project

Open the project folder in Visual Studio Code.

### 2. Install dependencies

Open the VS Code terminal and execute:

```bash
pip install -r requirements
```

### 3. Install required libraries manually (if needed)

```bash
pip install torch transformers
```

### 4. Run the program

Execute the following command:

```bash
python main.py
```

## Execution

When the program runs:

1. The GPT-2 model starts loading.
2. The tokenizer is initialized.
3. The pretrained language model is loaded.
4. Text processing and generation are performed according to the program.
5. Probability-related results can be stored in the CSV file.

The model may download pretrained files during its first execution. An internet connection is required for the initial download.

## Expected Outcome

- Successful loading of the pretrained GPT-2 model.
- Tokenization and processing of text inputs.
- Language generation using GPT-2.
- Probability-related analysis and CSV results, as implemented in the program.

## Troubleshooting

**1. OpenBLAS Memory Allocation Error**

Try limiting numerical-library threads:

```powershell
$env:OPENBLAS_NUM_THREADS="1"
$env:OMP_NUM_THREADS="1"
```

**2. PyTorch Memory Error**

- Close unnecessary applications.
- Restart VS Code.
- Check available RAM and Windows virtual memory.
- Verify that PyTorch imports correctly.

**3. Missing Dependencies**

Run:

```bash
pip install -r requirements
```

**4. Model Download Error**

Check your internet connection and try running the program again.

## Conclusion

This Week 7 project demonstrates the use of a pretrained GPT-2 language model with PyTorch and Hugging Face Transformers. It provides practical experience with language-model loading, tokenization, text generation, and probability-related result handling.

---

**Project:** Week 7 – GPT-2 Language Model and Probability Analysis  
**Language:** Python  
**Model:** GPT-2  
**Framework:** PyTorch and Hugging Face Transformers