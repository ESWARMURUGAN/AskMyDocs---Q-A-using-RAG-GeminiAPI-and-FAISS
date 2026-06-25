from config import client, GENERATION_MODEL


def generate_answer(query, chunks):
    context = "\n\n".join(chunk["text"] for chunk in chunks)

    prompt = f"""Answer the question using only this context.

Context:
{context}

Question: {query}"""

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt
    )
    return response.text
