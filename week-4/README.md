Tokenizer Comparison

This project compares how three different tokenizers split the same sentence into tokens. It uses a sentence in English, Telugu and Hindi, so you can see how each tokenizer handles each language.

Tokenizers Used
BPE (GPT-2): model name gpt2
WordPiece (Multilingual BERT): model name bert-base-multilingual-cased
SentencePiece (XLM-R): model name xlm-roberta-base
Languages Used
English: Artificial intelligence is changing the world.
Telugu: కృత్రిమ మేధస్సు ప్రపంచాన్ని మారుస్తోంది.
Hindi: कृत्रिम बुद्धिमत्ता दुनिया को बदल रही है।
Files
tokenizer_comparison.py: the main program
requirements_1.txt: list of packages to install
Setup

Step 1: Install the packages

pip install -r requirements_1.txt

Step 2: Make sure you have internet the first time you run it. The tokenizers are downloaded from Hugging Face and saved on your computer. After that, they load from your computer.

Run

python tokenizer_comparison.py

What You Will See

For each language and each tokenizer, the program prints:

Tokens: the pieces the sentence was split into
Token IDs: the number given to each token
Token count: the total number of tokens
Why This Is Useful

A tokenizer that was not trained well on a language splits its words into many small pieces. More tokens means more cost and less space for your text in the model. Comparing the token counts shows which tokenizer works best for each language.
