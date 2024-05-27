# config.py
CHROMA_PATH = "chroma"
DATA_PATH = "data"
EMBEDDING_MODEL_NAME = "mxbai-embed-large"
LLM_MODEL_NAME = "phi3:mini"
PROMPT_TEMPLATE = """
Answer the question using these reference information:

{context}

---

Answer the question based on the above context: {question}
"""
