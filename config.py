import os
from google import genai

API_KEY = ""  # Replace with your actual API key
client = genai.Client(api_key=API_KEY)

EMBEDDING_MODEL = "gemini-embedding-001"
GENERATION_MODEL = "gemini-2.5-flash"

CHUNK_SIZE = 500   # characters per chunk
TOP_K = 3          # how many chunks to retrieve per question
