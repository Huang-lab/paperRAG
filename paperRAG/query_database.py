# paperRAG/query_database.py

from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from .embeddings import get_embedding_function
from .config import CHROMA_PATH, LLM_MODEL_NAME, PROMPT_TEMPLATE


def query_rag(query_text: str, num_queries: int):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH,
                embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=num_queries)
    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc, _score in results])

    # Alternative search method, works pretty similarly
    # results = db.max_marginal_relevance_search(
    #     query_text, k=num_queries, fetch_k=num_queries*3)
    # context_text = "\n\n---\n\n".join(
    #     [doc.page_content for doc in results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = Ollama(model=LLM_MODEL_NAME)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text
