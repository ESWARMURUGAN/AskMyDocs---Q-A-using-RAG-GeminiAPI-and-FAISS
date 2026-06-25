from document_loader import load_and_chunk
from embeddings import get_embedding
from vector_store import add_to_store
from retrieval import retrieve
from generation import generate_answer

# 1. load and chunk documents
chunks = load_and_chunk("documents")
print(f"Loaded {len(chunks)} chunks")

# 2. embed every chunk and store it
for chunk in chunks:
    chunk["embedding"] = get_embedding(chunk["text"])
add_to_store(chunks)
print("Embeddings stored")

# 3. ask a question
query = input("Enter your question: ")

# 4. retrieve relevant chunks
relevant_chunks = retrieve(query)

# 5. generate an answer using those chunks
answer = generate_answer(query, relevant_chunks)
print("\nAnswer:")
print(answer)