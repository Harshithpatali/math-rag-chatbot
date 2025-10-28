# 🧮 Math RAG Chatbot

<div align="center">

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com/)
[![FAISS](https://img.shields.io/badge/FAISS-00C7B7?style=for-the-badge&logo=vector&logoColor=white)](https://faiss.ai/)

An intelligent **Retrieval-Augmented Generation (RAG)** chatbot specialized in answering questions from **Linear Algebra textbooks** with academic precision.

*Built for students, educators, and mathematics enthusiasts*

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🔍 Intelligent Retrieval** | FAISS-powered semantic search across textbook content |
| **🧠 Context-Aware Generation** | Google FLAN-T5 model for accurate, educational responses |
| **📚 Subject Specialization** | Fine-tuned for Linear Algebra concepts and terminology |
| **🚀 High Performance** | Local vector store for fast, offline-capable search |
| **🎯 User-Friendly Interface** | Clean Streamlit chat interface with conversation history |
| **☁️ Multi-Platform Deployment** | Docker, GCP, and Streamlit Cloud ready |

---

## 🏗️ Architecture Overview
User Question → Streamlit UI → Sentence Transformer Embeddings → FAISS Vector Store
↓
Context Retrieval → FLAN-T5 Model → Generated Answer → Streamlit UI

text

---

## 🛠️ Tech Stack

### **Frontend & Deployment**
- **Streamlit** - Interactive web application framework
- **Docker** - Containerization for consistent deployments
- **Google Cloud Platform** - Cloud deployment infrastructure
- **Streamlit Cloud** - Alternative hosting solution

### **AI & ML Components**
- **LangChain** - Framework for developing RAG applications
- **FAISS** (Facebook AI Similarity Search) - Vector database for efficient similarity search
- **Sentence Transformers** (`all-MiniLM-L6-v2`) - Text embedding model
- **Google FLAN-T5** - Instruction-tuned text generation model

### **Core Libraries**
- **Transformers** - Hugging Face model inference
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation
- **Sentence-Transformers** - Embedding generation

---

## 📁 Project Structure
math_rag_chatbot/
├── 📄 app.py # Main Streamlit application
├── 📄 requirements.txt # Python dependencies
├── 📄 Dockerfile # Docker container configuration
├── 📄 .dockerignore # Docker ignore patterns
├── 📁 index/ # FAISS vector store directory
│ ├── 📄 index.faiss # FAISS index file
│ └── 📄 index.pkl # Index metadata
└── 📄 README.md # Project documentation

text

---

## 🚀 Quick Start

### **Local Development**

#### 1. Clone & Setup
```bash
# Clone the repository
git clone https://github.com/your-username/math_rag_chatbot.git
cd math_rag_chatbot

# Create virtual environment
python -m venv rag_env

# Activate environment
# Windows:
rag_env\Scripts\activate
# macOS/Linux:
source rag_env/bin/activate

# Install dependencies
pip install -r requirements.txt
2. Run the Application
bash
streamlit run app.py
🌐 Access at: http://localhost:8501

🐳 Docker Deployment
1. Build the Image
bash
docker build -t math-rag-chatbot .
2. Run the Container
bash
docker run -p 8501:8501 math-rag-chatbot
3. Access the Application
Open your browser and navigate to http://localhost:8501

☁️ Cloud Deployment
Google Cloud Platform (GCP)
Enable Required Services

bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
Build and Deploy

bash
# Build container image
gcloud builds submit --tag gcr.io/your-project-id/math-rag-chatbot

# Deploy to Cloud Run
gcloud run deploy math-rag-chatbot \
  --image gcr.io/your-project-id/math-rag-chatbot \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
Streamlit Cloud
Push your code to GitHub

Visit share.streamlit.io

Connect your GitHub repository

Set app.py as the main file path

Click Deploy

💡 Example Queries
Try these sample questions to test the chatbot:

"Explain eigenvalues and eigenvectors in simple terms with an example."

"What is the geometric interpretation of the determinant?"

"How do you find the rank of a matrix and why is it important?"

"Compare and contrast null space and column space."

"What are the applications of singular value decomposition?"

🔧 Configuration
Environment Variables
Create a .env file for configuration:

env
# Model Configuration
MODEL_NAME=google/flan-t5-base
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Vector Store
INDEX_PATH=index/
SIMILARITY_TOP_K=3

# Application
MAX_HISTORY=5
TEMPERATURE=0.7
Customizing for Other Subjects
To adapt this chatbot for other academic subjects:

Replace the FAISS index with your subject-specific documents

Update the embedding model if needed for domain-specific terminology

Modify the system prompts in app.py to reflect the new subject

🎯 How It Works
1. Question Processing
User input is converted to embeddings using Sentence Transformers

Semantic search identifies relevant textbook passages

2. Context Retrieval
FAISS performs similarity search across vector database

Top-k most relevant contexts are retrieved

3. Answer Generation
FLAN-T5 model generates responses using retrieved context

Response is formatted for educational clarity

4. User Interface
Streamlit provides real-time chat interface

Conversation history is maintained during session

📊 Performance
Metric	Value
Response Time	< 5 seconds
Accuracy	Context-dependent, high for textbook content
Scalability	Supports multiple concurrent users
Index Size	~400MB (depending on textbook content)
🤝 Contributing
We welcome contributions! Please see our contributing guidelines for details.

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Harshith Devraj

📧 Email: harshikollur302@gmail.com

🎓 Education: M.Sc. Applied Mathematics & Computing, Manipal Academy of Higher Education

💼 LinkedIn: Harshith Devraj

🐙 GitHub: @harshithdevraj

🙏 Acknowledgments
Hugging Face for the Transformers library and model hosting

Meta AI for the FAISS library

Streamlit for the excellent deployment platform

Google Research for the FLAN-T5 model

