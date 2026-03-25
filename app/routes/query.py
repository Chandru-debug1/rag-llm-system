from fastapi import APIRouter
from app.services.rag_pipeline import RAGPipeline

router = APIRouter()
rag = RAGPipeline()

@router.post("/ask")
def ask_question(query: str):
    answer = rag.query(query)
    return {"response": answer}