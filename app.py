import streamlit as st
from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import SentenceTransformerEmbeddings

# 1️⃣ Load FAISS index
@st.cache_resource
def load_faiss_index():
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.load_local("index", embeddings, allow_dangerous_deserialization=True)
    return db

# 2️⃣ Load QA model
@st.cache_resource
def load_qa_model():
    return pipeline(
        "text2text-generation", 
        model="google/flan-t5-base", 
        device=-1,
        max_length=512
    )

def simple_rag_query(query, db, qa_model, k=3):
    # Retrieve relevant documents
    docs = db.similarity_search(query, k=k)
    
    # Combine context from documents
    context = "\n".join([doc.page_content for doc in docs])
    
    # Create enhanced prompt for better math responses
    prompt = f"""You are a mathematics tutor. Based on the following context from a Linear Algebra textbook, provide a clear and accurate answer to the question.

Context information:
{context}

Question: {query}

Please provide a helpful and educational answer based on the context:"""
    
    # Generate answer
    result = qa_model(
        prompt, 
        max_length=512, 
        do_sample=False,
        temperature=0.1
    )
    return result[0]['generated_text']

# Initialize components
db = load_faiss_index()
qa_model = load_qa_model()

# Streamlit UI
st.title("📘 Math RAG Chatbot")
st.write("Ask me anything about your Linear Algebra textbook!")
st.markdown("---")

query = st.text_input("Enter your question:")

if query:
    with st.spinner("🔍 Searching through textbook..."):
        try:
            answer = simple_rag_query(query, db, qa_model)
            
            st.success("💡 Answer:")
            st.write(answer)
            
            # Show source documents (optional)
            with st.expander("📚 View source documents"):
                docs = db.similarity_search(query, k=3)
                for i, doc in enumerate(docs):
                    st.markdown(f"**Source {i+1}:**")
                    st.text(doc.page_content[:300] + "..." if len(doc.page_content) > 300 else doc.page_content)
                    st.markdown("---")
                    
        except Exception as e:
            st.error(f"Error: {str(e)}")