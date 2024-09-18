# paperRAG/query_database.py
import time
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain.retrievers import EnsembleRetriever
from langchain_community.retrievers import BM25Retriever
from .embeddings import get_embedding_function
from .populate_database import load_documents
from .config import CHROMA_PATH


def query_rag(query_text: str, num_queries: int, llm_model_name: str, embed_model_name: str, prompt_template: str):
    # Prepare the DB & search by ensemble and rerank the results based on the Reciprocal Rank Fusion algorithm https://python.langchain.com/v0.1/docs/modules/data_connection/retrievers/ensemble/
    keyword_weight = 0.2
    vector_weight = 1 - keyword_weight
    documents = load_documents()
    vector_db = Chroma(persist_directory=CHROMA_PATH,
                       embedding_function=get_embedding_function(embed_model_name))

    # Set up retrievers
    vector_retriever = vector_db.as_retriever(
        search_type="similarity", search_kwargs={"k": num_queries})
    keyword_retriever = BM25Retriever.from_texts(
        [doc.page_content for doc in documents])
    keyword_retriever.k = num_queries

    # Combine retrievers
    ensemble_retriever = EnsembleRetriever(
        retrievers=[keyword_retriever, vector_retriever], weights=[keyword_weight, vector_weight])

    results = ensemble_retriever.invoke(query_text)

    # Combine the results into a single context text
    context_text = "\n\n---\n\n".join(
        [doc.page_content for doc in results])

    prompt_template = ChatPromptTemplate.from_template(prompt_template)
    prompt = prompt_template.format(context=context_text, question=query_text)
    #print(prompt)

    # Measure the time taken to generate the response
    start_time = time.time()
    model = Ollama(model=llm_model_name) # QUESTION: Why do we initialize the model for each query?
    response_text = model.invoke(prompt)
    end_time = time.time()

    elapsed_time = end_time - start_time
    print(
        f"{llm_model_name} response generation time: {elapsed_time:.2f} seconds"
    )

    sources = [doc.metadata.get("id", None) for doc in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text
