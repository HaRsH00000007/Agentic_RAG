# utils.py
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, SummaryIndex
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.tools import QueryEngineTool, FunctionTool
from llama_index.core.vector_stores import MetadataFilters, FilterCondition
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.google_genai import GoogleGenAI
from typing import List, Optional

def get_doc_tools(file_path: str, name: str, gemini_api_key: str):
    """Get vector and summary tools for a document using Gemini."""
    
    llm = GoogleGenAI(api_key=gemini_api_key, model="models/gemini-2.0-flash")
    embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    documents = SimpleDirectoryReader(input_files=[file_path]).load_data()
    splitter = SentenceSplitter(chunk_size=1024)
    nodes = splitter.get_nodes_from_documents(documents)
    
    vector_index = VectorStoreIndex(nodes, embed_model=embed_model)
    
    def vector_query(query: str, page_numbers: Optional[List[str]] = None) -> str:
        page_numbers = page_numbers or []
        metadata_dicts = [{"key": "page_label", "value": p} for p in page_numbers]
        
        query_engine = vector_index.as_query_engine(
            similarity_top_k=2,
            filters=MetadataFilters.from_dicts(
                metadata_dicts,
                condition=FilterCondition.OR
            ),
            llm=llm
        )
        response = query_engine.query(query)
        return str(response)
    
    vector_query_tool = FunctionTool.from_defaults(
        name=f"vector_query_{name}",
        fn=vector_query,
        description=f"Search for specific information in the {name} document. Provide a query and optional page numbers."
    )
    
    summary_index = SummaryIndex(nodes)
    summary_query_engine = summary_index.as_query_engine(
        response_mode="tree_summarize",
        use_async=True,
        llm=llm
    )
    
    summary_tool = QueryEngineTool.from_defaults(
        name=f"summarize_{name}",
        query_engine=summary_query_engine,
        description=f"Get a holistic summary of the {name} document."
    )
    
    return vector_query_tool, summary_tool