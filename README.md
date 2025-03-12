# Agentic_RAG

Agentic RAG System with LlamaIndex, Gemini, and Hugging Face Embeddings

Overview

This repository contains an Agentic Retrieval-Augmented Generation (RAG) system built using LlamaIndex, Gemini, and Hugging Face embeddings. The system efficiently retrieves relevant documents and enhances LLM responses by integrating knowledge from external sources.

Features

> Smart Query Handling – Dynamically chooses the best method (retrieval or summarization) instead of blindly fetching documents.

> Better Efficiency – Reduces unnecessary retrievals, making responses faster and more relevant.

> Higher Adaptability – Adjusts responses based on different types of queries rather than following a rigid retrieval structure.

> Improved Accuracy – Prevents hallucinations by ensuring that only the most relevant information is used for generation.

Tech Stack

> LlamaIndex: For document indexing and retrieval.

> Gemini API: For generative responses.

> Hugging Face Transformers: For embedding-based retrieval.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
!([image_url](https://github.com/HaRsH00000007/Agentic_RAG/blob/a6a75fade4926dc4fd01938f85ec9b9f09939d16/Screenshot%202025-03-12%20163654.png))
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Usage

> Set up API keys:

> Obtain your Gemini API key from Google.

> Set environment variables:

> export GEMINI_API_KEY='your-api-key'

> Example Query

> User Input: "What is Retrieval-Augmented Generation?"

> System Response: "Retrieval-Augmented Generation (RAG) is a framework that enhances LLM outputs by fetching relevant external documents..."

Contributing

Feel free to open issues, submit PRs, or suggest improvements!

License

This project is licensed under the MIT License.

🚀 Happy Coding!
