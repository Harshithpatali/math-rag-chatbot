# 🧮 Math RAG Chatbot

An intelligent **Retrieval-Augmented Generation (RAG)** chatbot specialized in answering questions from **Linear Algebra textbooks** with academic precision. Built for **students, educators, and mathematics enthusiasts**, it combines retrieval-based search with generative AI for accurate, contextual, and step-by-step mathematical explanations.

---

## ✨ Features

- 🔍 **Intelligent Retrieval:** FAISS-powered semantic search across textbook content  
- 🧠 **Context-Aware Generation:** FLAN-T5 model ensures accurate, educational responses  
- 📚 **Subject Specialization:** Tuned for Linear Algebra and mathematical terminology  
- 🚀 **High Performance:** Local FAISS vector store for fast, offline-capable search  
- 🎯 **User-Friendly Interface:** Streamlit chat UI with conversation history  
- ☁️ **Multi-Platform Deployment:** Ready for Docker, Google Cloud Run, and Streamlit Cloud  

---

## 🏗️ Architecture Overview

**Flow:**  
User Query → Embedding Generation (Sentence Transformers) → FAISS Vector Search → Context Retrieval → FLAN-T5 Response → Streamlit UI  

---

## 🛠️ Tech Stack

| Layer | Technologies |
|--------|---------------|
| **Frontend & UI** | Streamlit |
| **RAG Framework** | LangChain |
| **Vector Store** | FAISS (Facebook AI Similarity Search) |
| **Embedding Model** | Sentence Transformers (`all-MiniLM-L6-v2`) |
| **Text Generation Model** | Google FLAN-T5 |
| **Core Libraries** | Transformers, NumPy, Pandas |
| **Deployment** | Docker, Google Cloud Run, Streamlit Cloud |
| **Environment** | Python 3.10+ |

---

## 📁 Project Structure

math_rag_chatbot/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── Dockerfile # Docker configuration
├── .dockerignore # Files ignored by Docker
├── index/ # FAISS vector index directory
│ ├── index.faiss
│ └── index.pkl
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Quick Start

### 🔧 Local Setup

```bash
# Clone the repository
git clone https://github.com/Harshithpatali/math-rag-chatbot.git
cd math-rag-chatbot

# Create and activate virtual environment
python -m venv rag_env
# macOS/Linux
source rag_env/bin/activate
# Windows
rag_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
Access the app at: http://localhost:8501

🐳 Docker Deployment
bash
Copy code
# Build Docker image
docker build -t math-rag-chatbot .

# Run the container
docker run -p 8501:8501 math-rag-chatbot
App runs at: http://localhost:8501

☁️ Google Cloud Deployment
bash
Copy code
# Enable required GCP services
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Build and push container image
gcloud builds submit --tag gcr.io/your-project-id/math-rag-chatbot

# Deploy to Cloud Run
gcloud run deploy math-rag-chatbot \
  --image gcr.io/your-project-id/math-rag-chatbot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
🌐 Streamlit Cloud Deployment
Push your project to GitHub

Go to Streamlit Cloud

Connect your GitHub repository

Set app.py as the main file

Click Deploy

⚙️ Configuration
Create a .env file in the root directory:

ini
Copy code
# Model Configuration
MODEL_NAME=google/flan-t5-base
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Vector Store
INDEX_PATH=index/
SIMILARITY_TOP_K=3

# Application
MAX_HISTORY=5
TEMPERATURE=0.7
💡 Example Queries
“Explain eigenvalues and eigenvectors in simple terms with an example.”

“What is the geometric interpretation of the determinant?”

“How do you find the rank of a matrix and why is it important?”

“Compare and contrast null space and column space.”

“What are the applications of singular value decomposition?”

🎯 How It Works
Question Processing: Converts user input into embeddings using Sentence Transformers

Context Retrieval: Uses FAISS to identify relevant textbook sections

Answer Generation: FLAN-T5 generates an answer based on retrieved context

User Interface: Streamlit displays the response interactively with chat history

📊 Performance
Metric	Value
Response Time	< 5 seconds
Accuracy	High (context-dependent)
Scalability	Supports multiple users
Index Size	~400 MB (depends on content)

🧱 Future Enhancements
🧮 Add LaTeX rendering for mathematical notation

📘 Expand to additional mathematical subjects

☁️ Integrate Hugging Face Inference API for scalability

🧠 Add fine-tuning pipeline for subject-specific improvements

🤝 Contributing
We welcome contributions!

bash
Copy code
# Create a new feature branch
git checkout -b feature/your-feature

# Commit changes
git commit -m "Add your feature"

# Push branch
git push origin feature/your-feature
Open a Pull Request and contribute 🚀

👨‍💻 Author
Harshith Devraj
📧 harshikollur302@gmail.com
🎓 M.Sc. Applied Mathematics & Computing — Manipal Academy of Higher Education
🐙 GitHub: @Harshithpatali

📝 License
This project is licensed under the MIT License.

🙏 Acknowledgments
Hugging Face — for Transformers & FLAN-T5

Meta AI — for FAISS library

Streamlit — for app and deployment

Google Cloud — for cloud hosting support

