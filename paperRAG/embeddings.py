from langchain_community.embeddings.ollama import OllamaEmbeddings
from .config import EMBEDDING_MODEL_NAME


def get_embedding_function():

    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL_NAME)
    return embeddings
