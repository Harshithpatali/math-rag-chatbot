import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma  # ✅ Use Chroma instead of FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

@st.cache_resource
def load_chroma_index():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory="chroma_index", embedding_function=embeddings)
    return db

st.title("📘 Math RAG Chatbot")
st.write("Ask me anything about your Linear Algebra textbook!")

db = load_chroma_index()
retriever = db.as_retriever()

pipe = pipeline("text2text-generation", model="google/flan-t5-base")
llm = HuggingFacePipeline(pipeline=pipe)

qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = st.text_input("Enter your question:")
if query:
    with st.spinner("Thinking..."):
        answer = qa.run(query)
    st.write("**Answer:**", answer)
