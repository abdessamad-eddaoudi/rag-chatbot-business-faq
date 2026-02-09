def retrieve_best_answer(query_embedding, embedder):
    """
    Returns the answer of the most similar document
    """
    best_idx = embedder.most_similar(query_embedding)
    return embedder.documents[best_idx]["answer"]
