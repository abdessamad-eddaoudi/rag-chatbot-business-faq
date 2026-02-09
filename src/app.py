# app.py
import streamlit as st
from loader import load_documents
from embedder import LocalEmbedder
from retriever import retrieve_best_answer

# Load docs and initialize embedder (run once)
docs = load_documents()
embedder = LocalEmbedder(docs)

st.title("RAG Chatbot Demo")
st.write("Ask a question and get answers from your documents!")

query = st.text_input("Your question:")

if query:
    query_emb = embedder.embed_query(query)
    answer = retrieve_best_answer(query_emb, embedder)
    st.write("**Answer:**", answer)
