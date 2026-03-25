from app.services.retriever import load_vectorstore
from app.services.generator import get_llm, generate_answer

class RAGPipeline:
    def __init__(self):
        self.db = load_vectorstore()
        self.llm = get_llm()

    def query(self, user_query):
        docs = self.db.similarity_search(user_query, k=3)
        context = "\n".join([doc.page_content for doc in docs])
        return generate_answer(self.llm, context, user_query)