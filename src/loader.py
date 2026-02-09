import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
DOCS_PATH = os.path.join(DATA_DIR, "documents.json")

def load_documents(path=DOCS_PATH):
    """Load documents (FAQs) from JSON"""
    with open(path, "r", encoding="utf-8") as f:
        docs = json.load(f)
    return docs

