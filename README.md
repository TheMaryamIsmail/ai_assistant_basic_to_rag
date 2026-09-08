# AI-Assistant-Basic-to-RAG-

# 🤖 AI Assistant: Basic to Retrieval-Augmented Generation (RAG)

Welcome to the **AI-Assistant-Basic-to-RAG** repository! This project serves as a step-by-step guide and practical implementation tracking the evolution of building an AI assistant—starting from a simple prompt-driven conversational model to a fully-featured, context-aware **Retrieval-Augmented Generation (RAG)** pipeline.

---

## 📌 Project Overview

Large Language Models (LLMs) are powerful out of the box, but they can suffer from knowledge cutoffs, lack domain-specific awareness, or produce hallucination errors. 

This repository demonstrates how to overcome these limitations step-by-step:
1. **Basic AI Assistant:** Standard LLM call using prompt engineering and system instructions.
2. **Context-Aware Assistant:** Passing short-term conversation context/history.
3. **RAG-Powered AI Assistant:** Connecting the model to custom external knowledge (PDFs, Markdown, text documents) via semantic vector embeddings and vector databases.

---

## 🚀 Key Features

- 💡 **Progressive Learning Path:** Clear stages moving from simple API calls to complex vector search workflows.
- 📄 **Document Processing:** Loaders and text splitters to process PDFs, `.txt`, or Markdown files.
- 🔍 **Semantic Search:** Vector embeddings for high-accuracy similarity search.
- ⚡ **Vector DB Integration:** Efficient retrieval of relevant knowledge snippets using vector stores (e.g., ChromaDB / FAISS).
- 💬 **Grounded Responses:** LLM generates accurate answers backed strictly by retrieved document context.

---

## 🏗️ RAG Architecture Workflow

[ Custom Documents ] ➡️ [ Text Chunks ] ➡️ [ Embedding Model ] ➡️ [ Vector Database ]
│
[ User Question ]    ➡️ [ Query Vector ] ➡️ [ Similarity Search ] ──────┘
│
▼
[ Grounded Context ] + [ User Prompt ] ➡️ [ LLM ] ➡️ [ Final Output Response ]


---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.8+
- **LLM Provider:** OpenAI / Hugging Face / Ollama
- **RAG Framework:** LangChain / LlamaIndex
- **Vector Database:** ChromaDB / FAISS
- **Embeddings Model:** `sentence-transformers` / OpenAI Embeddings

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/TheMaryamIsmail/AI-Assistant-Basic-to-RAG-.git](https://github.com/TheMaryamIsmail/AI-Assistant-Basic-to-RAG-.git)
cd AI-Assistant-Basic-to-RAG-
2. Create a Virtual Environment
Bash
# On Linux/macOS
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
3. Install Required Libraries
Bash
pip install -r requirements.txt
(If requirements.txt is missing, install the core dependencies directly:)

Bash
pip install langchain langchain-community chromadb sentence-transformers openai python-dotenv
4. Configure Environment Variables
Create a .env file in the root directory and add your API keys:

Code snippet
OPENAI_API_KEY=your_openai_api_key_here
# Optional: Hugging Face or other keys depending on the model used
HF_TOKEN=your_huggingface_token_here
💻 Usage
1. Basic AI Assistant
Run the basic script/notebook to see a standard prompt-response loop:

Bash
python basic_assistant.py
2. Document Ingestion & Vector Storage
Add your target documents into the designated data/ directory and run the ingestion process to generate vector embeddings:

Bash
python ingest_documents.py
3. Querying the RAG System
Ask questions against your imported documents:

Bash
python rag_assistant.py --query "What is the key takeaways from the uploaded document?"
📂 Repository Structure
G-Code
AI-Assistant-Basic-to-RAG/
├── data/                    # Put your custom PDFs/txt files here
├── notebooks/               # Step-by-step Jupyter notebooks
│   ├── 01_basic_assistant.ipynb
│   ├── 02_prompt_engineering.ipynb
│   └── 03_rag_pipeline.ipynb
├── vector_store/            # Local directory where vector DB index is saved
├── .env.example             # Template for API keys
├── .gitignore               # Ignored files (API keys, venv, vector DB cached files)
├── ingest.py                # Script to load & embed documents into Vector DB
├── app.py                   # Main script/API server to run the AI assistant
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
🤝 Contributing
Contributions are always welcome! If you have suggestions to improve the RAG pipeline, add web UI support (Streamlit/Gradio), or optimize chunking techniques:

Fork the repository

Create a new Feature Branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📜 License
This repository is licensed under the MIT License.

👩‍💻 Author
Developed with ❤️ by Maryam Ismail.

If you find this repository useful, feel free to give it a ⭐!


## 🏗️ RAG Architecture Workflow

<img src="https://github.com/user-attachments/assets/9c03dbab-c3ac-4783-9608-bd986ec5b2a1" alt="RAG Architecture" width="100%" />

---

## 💻 Visual Demos

### Basic Conversational Assistant
<img src="https://github.com/user-attachments/assets/87d9555c-f7f5-4e53-8be9-d8b34cd960e0" alt="Basic Chat Demo" width="100%" />


