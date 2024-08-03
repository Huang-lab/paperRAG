from langchain_community.embeddings.ollama import OllamaEmbeddings


def get_embedding_function(embed_model_name: str):
    embeddings = OllamaEmbeddings(model=embed_model_name)
    return embeddings
