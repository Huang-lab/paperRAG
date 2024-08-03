import argparse
import time
from .query_database import query_rag
from .populate_database import clear_database, load_documents, split_documents, add_to_chroma


def main():
    parser = argparse.ArgumentParser(
        description="Indicate whether you'd like to populate the database or query via RAG+LLM")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the populate command
    populate_parser = subparsers.add_parser(
        "populate", help="Populate the database")
    populate_parser.add_argument(
        "--reset", action="store_true", help="Reset the database")
    populate_parser.add_argument(
        "--embed_model", type=str, default="mxbai-embed-large", help="Embedding model name")

    # Subparser for the query command
    query_parser = subparsers.add_parser("query", help="Query the database")
    query_parser.add_argument("query_text", type=str, help="The query text")
    query_parser.add_argument(
        "--num_queries", type=int, default=5, help="Number of queries to perform")
    query_parser.add_argument(
        "--llm_model", type=str, default="llama3.1", help="LLM model name")
    query_parser.add_argument(
        "--embed_model", type=str, default="mxbai-embed-large", help="Embedding model name")
    query_parser.add_argument(
        "--prompt_template", type=str, default="""
Answer the question using the relevant parts of this information:

{context}

---

Answer the question based on relevant parts of the above context: {question}
Be thorough and provide precise answers.
""", help="Prompt template")

    args = parser.parse_args()

    if args.command == "populate":
        start_time = time.time()

        if args.reset:
            print("✨ Clearing Database")
            clear_database()

        documents = load_documents()
        chunks = split_documents(documents)
        add_to_chroma(chunks, embed_model_name=args.embed_model)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total population time: {elapsed_time:.2f} seconds")

    elif args.command == "query":
        start_time = time.time()

        query_rag(args.query_text, num_queries=args.num_queries,
                  llm_model_name=args.llm_model, embed_model_name=args.embed_model, prompt_template=args.prompt_template)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total query time: {elapsed_time:.2f} seconds")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
