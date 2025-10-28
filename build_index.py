from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# 1️⃣ Load PDF
loader = PyPDFLoader("data/linear_algebra.pdf")
documents = loader.load()

# 2️⃣ Split text into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = splitter.split_documents(documents)

# 3️⃣ Create embeddings
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 4️⃣ Store in FAISS
db = FAISS.from_documents(texts, embeddings)
db.save_local("index")

print("✅ FAISS index built and saved to /index/")
