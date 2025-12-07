

# 🚀 Local AI Agent with Python (Ollama + LangChain + RAG)

Build your own **local, private, and free AI agent** powered by **Ollama**, **LangChain**, and **ChromaDB**.
This project runs **100% locally** — no API keys, no cloud, no cost! 🎉

---

## 📌 Features

✨ **Fully Local AI Agent**
✨ **Uses Ollama LLMs (Llama, Mistral, etc.)**
✨ **RAG Pipeline with ChromaDB**
✨ **Document Embedding & Semantic Search**
✨ **LangChain Integration**
✨ **Simple Python Codebase**
✨ **Open-source & beginner friendly**

---

## 🧰 Tech Stack

| Tool          | Purpose         |
| ------------- | --------------- |
| 🐍 Python     | Core logic      |
| 🤖 Ollama     | Local LLM       |
| 🔗 LangChain  | LLM pipeline    |
| 🧠 ChromaDB   | Vector database |
| 📄 Embeddings | Text retrieval  |

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/local-ai-agent
cd local-ai-agent
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Install & Run Ollama

Download Ollama 👉 [https://ollama.com/](https://ollama.com/)

Pull the model you want (example: Llama 3):

```bash
ollama pull llama3
```

Verify installation:

```bash
ollama run llama3
```

---

## 🏗️ Project Structure

```
📁 local-ai-agent/
│── app.py
│── vector_store.py
│── ai_agent.py
│── requirements.txt
│── README.md
│── data/
│     └── documents/
```

---

## ▶️ Running the Project

Start the AI agent:

```bash
python app.py
```

You can now ask questions like:

> “Explain this PDF’s content.”
> “Summarize the article.”
> “Search my documents for topics related to Python.”

---

## 📚 How It Works

### 🔹 Step 1 — Load documents

PDF/Text files → Text chunks

### 🔹 Step 2 — Create embeddings

LLM embeddings stored inside **ChromaDB**

### 🔹 Step 3 — Retrieve relevant chunks

Semantic search (vector similarity)

### 🔹 Step 4 — Send context to LLM

RAG (Retrieval-Augmented Generation)

### 🔹 Step 5 — LLM generates answer

Local, fast, and private 🤫

---
