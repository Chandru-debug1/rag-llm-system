from fastapi import FastAPI
from app.routes.query import router

app = FastAPI(title="RAG LLM System")

app.include_router(router)