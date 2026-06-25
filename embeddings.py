from google.genai import types
from config import client, EMBEDDING_MODEL


def get_embedding(text, task_type="RETRIEVAL_DOCUMENT"):
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(task_type=task_type)
    )
    return result.embeddings[0].values