# 🦾🚀 Nexus Agent v2

**Nexus Agent v2** is a stateful, high-performance **Agentic RAG (Retrieval-Augmented Generation)** system.

Unlike standard RAG scripts, v2 is built as a **scalable microservice** featuring persistent memory, cloud-native vector search, and advanced data preprocessing.

---

# 🌟 Key Features

### 🧠 Stateful Conversational Memory

Implements **RedisChatMessageHistory** to maintain multi-turn context across server restarts.

### 📄 Hybrid Data Ingestion

Advanced preprocessing for **PDFs** (Recursive Splitting) and **CSVs** (Pandas-based cleaning) ensuring high-fidelity context retrieval.

### 🤖 Local LLM Orchestration

Powered by **Llama-3.2:3b via Ollama** for privacy and offline inference.

### ☁️ Cloud-Native Vector Storage

Uses **Pinecone** to manage **3072-dimensional embeddings** with sub-second semantic search.

### 🔌 RESTful API Architecture

Built with **Flask** and designed for easy integration with frontend dashboards like **Streamlit**.

---

# 🏗️ System Architecture

### 1️⃣ Ingestion

Files are processed via `ingest.py`.

* CSVs are cleaned using **Pandas** to remove noise
* PDFs are chunked with **100-character overlap** to preserve semantic context

---

### 2️⃣ Vectorization

Text chunks are converted into vectors using **Ollama Embeddings** and stored in **Pinecone**.

---

### 3️⃣ State Management

User sessions are tracked in **Redis (Upstash)** using `session_id`, allowing the agent to remember names and previous facts across API calls.

---

### 4️⃣ Retrieval & Generation

Uses **LangChain RunnableWithMessageHistory** to combine:

* Retrieved context
* Chat history
* User query

into a single structured prompt for the LLM.

---

# 🛠️ Tech Stack

| Category        | Technology         |
| --------------- | ------------------ |
| Framework       | Flask              |
| LLM Framework   | LangChain (LCEL)   |
| LLM             | Ollama (Llama-3.2) |
| Embeddings      | Ollama Embeddings  |
| Vector DB       | Pinecone           |
| Memory          | Redis (Upstash)    |
| Data Processing | Pandas             |
| DevOps          | Docker             |
| Config          | `.env`             |

---

# 🚀 Getting Started

## 1️⃣ Prerequisites

Make sure you have:

* **Ollama installed**
* **llama3.2 model pulled**
* **Pinecone API key**
* **Redis / Upstash instance**

---

## 2️⃣ Environment Setup

Create a `.env` file:

```env
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME=your_index
REDIS_URL=rediss://default:password@endpoint:port
```

---

## 3️⃣ Installation

```bash
pip install -r requirements.txt
python main.py
```

---

# 📊 API Endpoints

| Method | Endpoint | Description                                          |
| ------ | -------- | ---------------------------------------------------- |
| POST   | `/nexus` | Upload files and query the agent with a `session_id` |

---

# 🧠 Example Workflow

```
User Uploads PDF/CSV
        ↓
Data Cleaning + Chunking
        ↓
Embeddings Generated
        ↓
Vectors Stored in Pinecone
        ↓
User Query
        ↓
Context Retrieval + Memory
        ↓
LLM Response
```

