# LangChain RAG & AI Applications

A comprehensive project demonstrating various LangChain implementations including Retrieval-Augmented Generation (RAG), chatbots, and API services using different embedding models and vector databases.

## Project Structure

```
├── .env                    # Environment variables (API keys)
├── .gitignore             # Git ignore file
├── docker-compose.yml     # Docker services configuration
├── requirement.txt        # Python dependencies
├── .vscode/
│   └── tasks.json        # VS Code task configurations
├── api/
│   ├── app.py            # FastAPI historical summary service
│   └── client.py         # API client
├── CHATBOT/
│   └── app.py            # Streamlit chatbot application
└── rag/
    ├── attention.pdf     # Research paper for RAG testing
    ├── chain.ipynb       # Advanced RAG chains & retrievers
    ├── docker-compose.yml # Weaviate database setup
    ├── sample.pdf        # Additional document for testing
    ├── simpleRAG.ipynb   # Basic RAG implementation
    └── speech.txt        # Text document for AI education content
```

## RAG pipeline flow

```
RAG Pipeline Flow:

User Query: "How does attention work?"
    ↓
RETRIEVER (db2.as_retriever())
    ↓ (searches vector database)
Retrieved Documents: [doc1, doc2, doc3]
    ↓
DOCUMENT CHAIN (LLM + Prompt + Documents)
    ↓ (generates answer using context)
Final Answer: "Attention works by..."
    ↓
RETRIEVAL CHAIN (orchestrates the whole process)
    ↓
Response: {
    "answer": "Attention works by...",
    "context": [doc1, doc2, doc3]
}
```

## Features

### 1. RAG (Retrieval-Augmented Generation)
- **Simple RAG**: Basic implementation with document loading, splitting, and querying
- **Advanced RAG**: Complex chains with multiple vector databases and embedding models
- **Multiple Data Sources**: Support for PDFs, text files, and web scraping
- **Vector Databases**: FAISS and Weaviate integration
- **Embedding Models**: Ollama and OpenAI embeddings

### 2. Chatbot Application
- Streamlit-based conversational AI
- Character-based responses (Arjun - Senior Software Engineer)
- Powered by Ollama's Gemma model

### 3. API Services
- FastAPI-based historical summary service
- RESTful endpoints for place/city historical overviews
- Ollama LLM integration

## Technologies Used

- **LangChain**: Core framework for LLM applications
- **Vector Databases**: FAISS, Weaviate
- **Embedding Models**: 
  - Ollama (llama2:7b, gemma3:4b)
  - OpenAI (text-embedding-3-small)
- **LLMs**: 
  - Ollama (Gemma, Llama2)
  - OpenAI GPT-3.5-turbo
- **Web Framework**: FastAPI, Streamlit
- **Document Processing**: PyPDF, BeautifulSoup
- **Infrastructure**: Docker, Docker Compose

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- Ollama installed locally
- OpenAI API key (optional)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LangChain
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Start Weaviate database (for advanced RAG)**
   ```bash
   cd rag
   docker-compose up -d
   ```

5. **Install and start Ollama**
   ```bash
   # Install Ollama from https://ollama.ai
   ollama pull gemma3:4b
   ollama pull llama2:7b
   ```

## Usage

### RAG Notebooks

1. **Simple RAG** ([`rag/simpleRAG.ipynb`](rag/simpleRAG.ipynb))
   - Basic document loading and processing
   - FAISS vector store implementation
   - Simple similarity search

2. **Advanced RAG** ([`rag/chain.ipynb`](rag/chain.ipynb))
   - Complex retrieval chains
   - Multiple embedding strategies
   - Weaviate integration
   - Document and retrieval chain combinations

### Chatbot Application

```bash
cd CHATBOT
streamlit run app.py
```

### API Service

```bash
cd api
python app.py
```

The API will be available at `http://localhost:8000` with endpoints:
- `POST /history` - Get historical summary of a place

## Key Components

### Document Loading & Processing
- **PDF Processing**: Using [`PyPDFLoader`](rag/simpleRAG.ipynb) for research papers
- **Web Scraping**: [`WebBaseLoader`](rag/simpleRAG.ipynb) for portfolio data
- **Text Splitting**: [`RecursiveCharacterTextSplitter`](rag/simpleRAG.ipynb) for optimal chunking

### Vector Stores & Embeddings
- **FAISS**: Local vector storage with Ollama embeddings
- **Weaviate**: Cloud-native vector database
- **Embedding Models**: Support for both local (Ollama) and cloud (OpenAI) embeddings

### Retrieval & Generation
- **Similarity Search**: Vector-based document retrieval
- **Retrieval Chains**: Advanced document processing pipelines
- **Prompt Templates**: Structured prompts for consistent responses

## 🔍 Example Usage

### Query Documents
```python
# Simple similarity search
query = "What is attention mechanism?"
results = db.similarity_search(query)
print(results[0].page_content)
```

### RAG Chain
```python
# Complete RAG pipeline
response = retrieval_chain.invoke({"input": "What is this paper about?"})
print(response['answer'])
```

##  Environment Variables

Required environment variables in [`.env`](.env):

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
```

##  Docker Support

The project includes Docker Compose configuration for:
- Weaviate vector database


## 🔗 Resources

- [LangChain Documentation](https://docs.langchain.com/)
- [Ollama](https://ollama.ai/)
- [Weaviate](https://weaviate.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Streamlit](https://streamlit.io/)

##  Project Highlights

- **Multi-modal RAG**: Support for various document types and data sources
- **Flexible Architecture**: Easy switching between embedding models and vector stores
- **Production Ready**: API services with proper error handling
- **Educational**: Well-documented notebooks for learning RAG concepts
- **Scalable**: Docker-based infrastructure for easy deployment

---
