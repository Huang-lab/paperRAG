# paperRAG/cli.py
import argparse
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

    # Subparser for the query command
    query_parser = subparsers.add_parser("query", help="Query the database")
    query_parser.add_argument("query_text", type=str, help="The query text")
    query_parser.add_argument(
        "--num_queries", type=int, default=10, help="Number of queries to perform")

    args = parser.parse_args()

    if args.command == "populate":
        if args.reset:
            print("✨ Clearing Database")
            clear_database()
        documents = load_documents()
        chunks = split_documents(documents)
        add_to_chroma(chunks)
    elif args.command == "query":
        query_rag(args.query_text, num_queries=args.num_queries)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
