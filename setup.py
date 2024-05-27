from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="paperRAG",
    version="0.1.0",
    author="Kuan-lin Huang",
    author_email="your.email@example.com",
    description="A RAG-llm tool for querying a database with PDF documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="TBD",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.123",
        "langchain-community>=0.0.6",
        "chromadb>=0.3.21",
        "PyPDF2>=3.0.1",
    ],
    entry_points={
        "console_scripts": [
            "paperrag=paperRAG.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
