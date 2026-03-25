from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embeddings

def create_vectorstore(chunks):
    embeddings = get_embeddings()
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("vectorstore")
    return db

def load_vectorstore():
    embeddings = get_embeddings()
    return FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)