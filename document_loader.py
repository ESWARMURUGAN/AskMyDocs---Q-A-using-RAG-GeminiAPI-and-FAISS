import os
from pypdf import PdfReader
from config import CHUNK_SIZE


def load_and_chunk(folder_path):
    chunks = []

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        # read the file's text depending on its type
        if filename.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        elif filename.endswith(".pdf"):
            reader = PdfReader(filepath)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        else:
            continue  # skip anything that isn't .txt or .pdf

        # cut the text into fixed-size chunks
        for i in range(0, len(text), CHUNK_SIZE):
            chunk_text = text[i:i + CHUNK_SIZE]
            chunks.append({"source": filename, "text": chunk_text})

    return chunks