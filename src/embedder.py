from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class LocalEmbedder:
    def __init__(self, documents):
        """
        documents: list of {"question": str, "answer": str}
        """
        self.documents = documents
        texts = [doc["question"] + " " + doc["answer"] for doc in documents]
        self.vectorizer = TfidfVectorizer()
        self.embeddings = self.vectorizer.fit_transform(texts).toarray()

    def embed_query(self, query):
        """Return embedding for a query"""
        return self.vectorizer.transform([query]).toarray()

    def most_similar(self, query_embedding):
        """Return index of most similar document"""
        similarities = np.dot(self.embeddings, query_embedding.T).flatten()
        best_idx = np.argmax(similarities)
        return best_idx
