import faiss
import numpy as np

# FAISS needs to know the vector size upfront.
# gemini-embedding-001 outputs 3072-dimensional vectors.
DIMENSION = 3072

# IndexFlatIP = exact search using Inner Product (dot product).
# Since our vectors are normalized, dot product == cosine similarity.
index = faiss.IndexFlatIP(DIMENSION)

# We also keep the original chunk dicts so we can return
# the text and source alongside the FAISS search results.
chunk_store = []


def add_to_store(chunks):
    vectors = []
    for chunk in chunks:
        vec = np.array(chunk["embedding"], dtype=np.float32)
        # normalize so dot product equals cosine similarity
        faiss.normalize_L2(vec.reshape(1, -1))
        vectors.append(vec)
        chunk_store.append(chunk)

    # stack all vectors into one matrix and add to the FAISS index
    matrix = np.vstack(vectors)
    index.add(matrix)


def search(query_embedding, top_k):
    vec = np.array(query_embedding, dtype=np.float32).reshape(1, -1)
    faiss.normalize_L2(vec)

    # D = similarity scores, I = indexes of matching chunks
    D, I = index.search(vec, top_k)

    results = []
    for score, idx in zip(D[0], I[0]):
        chunk = dict(chunk_store[idx])
        chunk["similarity"] = float(score)
        results.append(chunk)

    return results