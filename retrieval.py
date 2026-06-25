from embeddings import get_embedding
from vector_store import search
from config import TOP_K


def retrieve(query):
    query_embedding = get_embedding(query, task_type="RETRIEVAL_QUERY")
    return search(query_embedding, TOP_K)
