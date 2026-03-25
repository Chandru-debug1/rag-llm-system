# RAG Pipeline & LLM-based Q&A System

## 🚀 Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline using LangChain, Hugging Face embeddings, and FastAPI.

It enables users to query documents and receive context-aware, accurate responses powered by LLMs.

---

## 🧠 Features

* Document ingestion & chunking
* Semantic search using FAISS
* Hugging Face embeddings
* LLM-based response generation
* FastAPI backend for querying

---

## 🏗️ Tech Stack

* Python
* LangChain
* Hugging Face Transformers
* FAISS
* FastAPI

---

## 📁 Project Structure

```
app/
├── core/
├── routes/
├── services/
├── utils/
data/
vectorstore/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```
git clone https://github.com/your-username/rag-llm-system.git
cd rag-llm-system
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add documents

Place `.txt` files inside:

```
data/raw/
```

### 5. Build vector database

```
python build_db.py
```

### 6. Run the API

```
uvicorn app.main:app --reload
```

---

## 🌐 API Endpoint

```
POST /ask
```

---

## 🔐 Notes

* `.env` file is excluded for security
* `vectorstore/` is ignored (can be regenerated)

---

## 💡 Future Improvements

* Chat UI (React)
* PDF ingestion
* Deployment (AWS/GCP)
* Streaming responses
