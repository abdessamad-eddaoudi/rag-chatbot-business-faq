# AI Customer Support Chatbot

## Problem
Small businesses spend too much time answering repetitive customer questions.

## Solution
This system automatically answers customer FAQs using AI embeddings (TF-IDF). 
Just type a question, and it returns the most relevant answer from the document database.

## Workflow
1. Load FAQs from `data/documents.json`
2. Create embeddings (locally using TF-IDF)
3. User types a query → system retrieves the most relevant answer
4. Answer is returned instantly

## Tech Stack
- Python 3.13
- scikit-learn (TF-IDF)
- NumPy

## Demo
2–3 minute demo video: https://www.loom.com/share/c8bb149ad2f34ea9b7c32c0572eca10b

