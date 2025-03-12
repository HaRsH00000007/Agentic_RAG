# Agentic_RAG

Agentic RAG System with LlamaIndex, Gemini, and Hugging Face Embeddings

Overview

This repository contains an Agentic Retrieval-Augmented Generation (RAG) system built using LlamaIndex, Gemini, and Hugging Face embeddings. The system efficiently retrieves relevant documents and enhances LLM responses by integrating knowledge from external sources.

Features

> Retrieval-Augmented Generation (RAG): Improves LLM responses by dynamically fetching relevant data.

> Agentic Behavior: Uses multiple agents to optimize retrieval and generation tasks.

> LlamaIndex Integration: Manages document indexing and retrieval.

> Gemini API Integration: Uses Google's Gemini LLM for enhanced text generation.

> Hugging Face Embeddings: Generates high-quality vector representations for document retrieval.

> Scalable and Modular Design: Easily customizable for various applications.

Tech Stack

> LlamaIndex: For document indexing and retrieval.

> Gemini API: For generative responses.

> Hugging Face Transformers: For embedding-based retrieval.


Installation

# Clone the repository
git clone https://github.com/yourusername/agentic-rag.git
cd agentic-rag

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Usage

Set up API keys:

Obtain your Gemini API key from Google.

Set environment variables:

export GEMINI_API_KEY='your-api-key'

Run the application:

python app.py

Interact with the RAG system via the Streamlit UI.

Project Structure

📦 agentic-rag
├── 📂 data                  # Dataset and documents for retrieval
├── 📂 src                   # Source code
│   ├── indexer.py           # Handles document indexing
│   ├── retriever.py         # Fetches relevant documents
│   ├── generator.py         # Calls Gemini API for response generation
│   ├── app.py               # Main application
├── 📄 requirements.txt       # Dependencies
├── 📄 README.md              # Documentation

Example Query

User Input: "What is Retrieval-Augmented Generation?"

System Response: "Retrieval-Augmented Generation (RAG) is a framework that enhances LLM outputs by fetching relevant external documents..."

Contributing

Feel free to open issues, submit PRs, or suggest improvements!

License

This project is licensed under the MIT License.

🚀 Happy Coding!
