import streamlit as st
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings
import torch

# ----------------------------
# 1️⃣ Load FAISS Index
# ----------------------------
@st.cache_resource
def load_faiss_index():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("index", embeddings, allow_dangerous_deserialization=True)
    return db

# ----------------------------
# 2️⃣ Load QA Model
# ----------------------------
@st.cache_resource
def load_qa_model():
    device = 0 if torch.cuda.is_available() else -1  # ✅ auto GPU if available
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
 # You can change to flan-t5-small for cloud
        device=device,
        max_length=512
    )

# ----------------------------
# 3️⃣ Simple RAG Logic
# ----------------------------
def simple_rag_query(query, db, qa_model, k=3):
    # Retrieve top-k relevant docs
    docs = db.similarity_search(query, k=k)
    context = "\n".join([doc.page_content for doc in docs])

    # Create prompt for T5
    prompt = f"""You are a helpful mathematics tutor.
Use the following Linear Algebra textbook context to answer the question accurately.

Context:
{context}

Question: {query}

Answer in a clear and educational manner:"""

    # Generate the answer
    result = qa_model(prompt, max_length=512, do_sample=False, temperature=0.1)
    return result[0]["generated_text"], docs

# ----------------------------
# 4️⃣ Streamlit UI
# ----------------------------
st.set_page_config(page_title="Math RAG Chatbot", page_icon="📘", layout="centered")

st.title("📘 Math RAG Chatbot")
st.markdown("Ask me anything about your **Linear Algebra textbook!**")
st.markdown("---")

db = load_faiss_index()
qa_model = load_qa_model()

query = st.text_input("Enter your question:")

if query:
    with st.spinner("🔍 Searching through textbook..."):
        try:
            answer, docs = simple_rag_query(query, db, qa_model)
            st.success("💡 **Answer:**")
            st.write(answer)

            with st.expander("📚 View Source Documents"):
                for i, doc in enumerate(docs):
                    content = doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content
                    st.markdown(f"**Source {i+1}:** {content}")
                    st.markdown("---")

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
