# 🏥 Medical Chatbot with LLMs, LangChain, Pinecone & Flask

A **Medical Chatbot** powered by **Large Language Models (LLMs)** that allows users to interact with a medical knowledge base through a simple web interface.

The project uses **LangChain** for the LLM/RAG workflow, **Pinecone** for vector storage and similarity search, **Groq** for fast LLM inference, and **Flask** to provide the web application interface.

---

## 📌 Project Overview

The goal of this project is to build an AI-powered medical question-answering chatbot that can retrieve relevant information from medical documents and generate useful responses using an LLM.

Instead of directly asking the LLM to answer every question from its general knowledge, this project follows a **Retrieval-Augmented Generation (RAG)** approach.

### How the system works

```text
User
  ↓
Flask Web Application
  ↓
User Medical Question
  ↓
LangChain
  ↓
Query Embedding
  ↓
Pinecone Vector Database
  ↓
Relevant Medical Documents
  ↓
Groq LLM
  ↓
Generated Response
  ↓
User
```

The chatbot first searches the medical knowledge base for relevant information and then provides that information to the LLM as context for generating the final response.

---

# 🚀 Features

* 🤖 AI-powered medical chatbot
* 💬 Interactive chat interface
* 📚 Medical document-based question answering
* 🔎 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Fast LLM inference using Groq
* 🗄️ Pinecone vector database integration
* 🔗 LangChain integration
* 🌐 Flask-based web application
* 🔐 Environment-variable based API key management
* ☁️ AWS deployment-ready configuration
* 🔄 GitHub Actions / deployment secrets support

---

# 🛠️ Technologies Used

| Technology                | Purpose                               |
| ------------------------- | ------------------------------------- |
| **Python**                | Main programming language             |
| **LangChain**             | LLM and RAG application framework     |
| **Groq**                  | LLM inference                         |
| **Pinecone**              | Vector database and similarity search |
| **Sentence Transformers** | Text embeddings                       |
| **Flask**                 | Backend web framework                 |
| **PyPDF**                 | Extracting text from PDF documents    |
| **python-dotenv**         | Managing environment variables        |
| **HTML/CSS/JavaScript**   | Frontend interface                    |
| **AWS**                   | Cloud/deployment infrastructure       |
| **GitHub Actions**        | CI/CD and deployment automation       |

---

# 🧠 What is RAG?

This project uses **Retrieval-Augmented Generation (RAG)**.

RAG combines:

1. **Document Retrieval**
2. **Vector Similarity Search**
3. **Large Language Model Generation**

Instead of relying only on the LLM's pre-trained knowledge, the application retrieves relevant information from the medical knowledge base.

### RAG Pipeline

```text
Medical PDF Documents
        ↓
Extract Text
        ↓
Split Text into Chunks
        ↓
Generate Embeddings
        ↓
Store Embeddings in Pinecone
        ↓
User asks a question
        ↓
Convert Question into Embedding
        ↓
Search Pinecone
        ↓
Retrieve Relevant Documents
        ↓
Send Context + Question to LLM
        ↓
Generate Answer
        ↓
Display Answer
```

---

# 🔍 How the Project Works

## Step 1 — Medical Documents

The project uses medical documents as the knowledge source.

PDF documents are processed using **PyPDF**.

The text is extracted from the documents and prepared for the embedding process.

---

## Step 2 — Text Chunking

Large documents are divided into smaller pieces called **chunks**.

This is important because:

* Large documents cannot efficiently be sent directly to an LLM.
* Smaller chunks improve semantic search.
* Relevant sections can be retrieved more accurately.

---

## Step 3 — Generate Embeddings

Each text chunk is converted into a numerical vector using an embedding model.

These vectors represent the semantic meaning of the text.

For example:

```text
Medical Text
     ↓
Embedding Model
     ↓
Numerical Vector
```

The project uses **Sentence Transformers** for generating embeddings.

---

## Step 4 — Store Embeddings in Pinecone

The generated embeddings are stored in **Pinecone**.

Pinecone works as the project's vector database.

It allows the application to perform similarity searches and retrieve the most relevant medical information for a user's question.

---

## Step 5 — User Asks a Question

The user enters a medical question through the Flask web interface.

Example:

```text
What are the symptoms of diabetes?
```

---

## Step 6 — Semantic Search

The user's question is converted into an embedding.

The application sends this vector to Pinecone.

Pinecone searches the stored vectors and returns the most relevant medical document chunks.

```text
User Question
      ↓
Question Embedding
      ↓
Pinecone Similarity Search
      ↓
Relevant Medical Information
```

---

## Step 7 — LLM Generates the Answer

The retrieved medical information is provided as context to the LLM through LangChain.

The LLM then generates a natural-language response.

```text
Retrieved Context
       +
User Question
       ↓
     Groq LLM
       ↓
Final Response
```

---

# ⚙️ Project Architecture

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Flask Web App    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    LangChain     │
                    └────────┬─────────┘
                             │
                    ┌────────▼─────────┐
                    │ Query Embedding  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Pinecone     │
                    │  Vector Database │
                    └────────┬─────────┘
                             │
                       Relevant Docs
                             │
                             ▼
                    ┌──────────────────┐
                    │    Groq LLM      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Generated Answer │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      User        │
                    └──────────────────┘
```

---

# 📂 Project Structure

A typical project structure looks like this:

```text
Medical_Chatbot/
│
├── app.py
├── store_index.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── src/
│   └── ...
│
├── data/
│   └── medical_book.pdf
│
├── templates/
│   └── chat.html
│
└── static/
    ├── style.css
    └── script.js
```

> The exact folder structure may vary depending on the implementation.

---

# 💻 Installation & Setup

## STEP 01 — Clone the Repository

```bash
git clone https://github.com/Shreyash065232/Medical_Chatbot.git
```

Move into the project directory:

```bash
cd Medical_Chatbot
```

---

## STEP 02 — Create a Conda Environment

Create a new Python environment:

```bash
conda create -n medibot python=3.10 -y
```

Activate the environment:

```bash
conda activate medibot
```

---

## STEP 03 — Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

# 🔐 STEP 04 — Configure Environment Variables

Create a `.env` file in the root directory.

```text
Medical_Chatbot/
│
├── .env
├── app.py
├── store_index.py
└── ...
```

Add your API credentials:

```env
PINECONE_API_KEY="your_pinecone_api_key_here"
GROQ_API_KEY="your_groq_api_key_here"
```

### ⚠️ Important

Never upload your `.env` file or API keys to GitHub.

Add `.env` to your `.gitignore` file:

```gitignore
.env
__pycache__/
*.pyc
```

---

# 🗄️ STEP 05 — Create Pinecone Index

Before running the chatbot, the medical document embeddings need to be stored in Pinecone.

Run:

```bash
python store_index.py
```

This process generally performs the following operations:

```text
Medical Documents
       ↓
Load Documents
       ↓
Extract Text
       ↓
Split Text
       ↓
Generate Embeddings
       ↓
Create/Connect Pinecone Index
       ↓
Upload Vectors
```

Once this process is completed, the medical knowledge base is available for semantic retrieval.

---

# ▶️ STEP 06 — Run the Application

Start the Flask application:

```bash
python app.py
```

The application will start on the local Flask server.

Open the localhost URL shown in your terminal, for example:

```text
http://localhost:8080
```

or:

```text
http://127.0.0.1:8080
```

---

# 💬 Example Usage

After opening the application, enter a medical question in the chatbot interface.

Example:

```text
User:
What are the common symptoms of diabetes?

Chatbot:
The response is generated using the retrieved information
from the medical knowledge base and the configured LLM.
```

The exact response depends on the documents stored in the vector database and the LLM configuration.

---


github-actions
```
