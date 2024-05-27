# paperRAG

paperRAG is a command-line interface (CLI) tool for populating and querying a database with PDF documents. It uses the LangChain library and the Chroma vector database to store and retrieve information from PDF files, and language model from OllaMa to generate answers to queries.

## Installation

1. Clone the repository: `git clone https://github.com/your_username/paperRAG.git`
2. Navigate to the project directory: `cd paperRAG`
3. Install Ollama from https://ollama.com/ and install your embedding / LLM models of choice
4. Install the package and its dependencies: `pip install .`
5. Check and modify the `config.yml` to change the models and settings
6. Replace the PDFs in the `data` directory to the ones you'd like to query & chat with

## Usage

paperRAG provides two main commands: `populate` and `query`.

### Populate the Database

To populate the database with PDF documents, use the `populate` command: `paperrag populate [--reset]`

- `--reset`: This optional flag will clear the existing database before populating it with new documents.

The `populate` command will load all PDF files from the `data` directory, split them into chunks, and add them to the Chroma vector database.

### Query the Database

To query the database, use the `query` command: `paperrag query "your query text" [--num_queries NUM]`

Replace `"your query text"` with the actual query you want to ask. The command will search the database for relevant chunks of text and generate an answer using the OllaMa language model.

- `--num_queries NUM`: This optional argument specifies the number of queries to perform. If not provided, the default value of `10` will be used.

The output will include the generated answer and the sources (document IDs) used to construct the answer.

## Configuration

The following configuration options are available in the `config.py` file:

- `DATA_PATH`: The directory where your PDF files are stored (default: `"data"`).
- `CHROMA_PATH`: The directory where the Chroma vector database will be stored (default: `"chroma"`).
- `EMBEDDING_MODEL_NAME`: The name of the embedding model to use (default: `"mxbai-embed-large"`).
- `LLM_MODEL_NAME`: The name of the language model (via OllaMa) to use (default: `"phi3:mini"`).
- `PROMPT_TEMPLATE`: The prompt template used for querying the language model.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
The initial version of this is largely inspired by https://github.com/pixegami/rag-tutorial-v2
Other reference:

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or issues, please open an issue.
