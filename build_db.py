from app.utils.loader import load_documents
from app.utils.chunking import split_documents
from app.services.retriever import create_vectorstore

docs = load_documents()
chunks = split_documents(docs)

create_vectorstore(chunks)

print("✅ Vector DB created!")