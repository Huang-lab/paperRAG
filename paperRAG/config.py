# config.py
CHROMA_PATH = "chroma"
DATA_PATH = "data"
EMBEDDING_MODEL_NAME = "mxbai-embed-large"
LLM_MODEL_NAME = "phi3:mini"
PROMPT_TEMPLATE = """
Answer the question using the relevant parts of this information:

{context}

---

Answer the question based on relevant parts of the above context: {question}
"""
