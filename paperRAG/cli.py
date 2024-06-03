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

    # Subparser for the query command
    query_parser = subparsers.add_parser("query", help="Query the database")
    query_parser.add_argument("query_text", type=str, help="The query text")
    query_parser.add_argument(
        "--num_queries", type=int, default=10, help="Number of queries to perform")

    args = parser.parse_args()

    if args.command == "populate":
        start_time = time.time()
        
        if args.reset:
            print("✨ Clearing Database")
            clear_database()
        
        documents = load_documents()
        chunks = split_documents(documents)
        add_to_chroma(chunks)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total population time: {elapsed_time:.2f} seconds")
    
    elif args.command == "query":
        start_time = time.time()
        
        query_rag(args.query_text, num_queries=args.num_queries)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Total query time: {elapsed_time:.2f} seconds")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()