from langchain_openai import ChatOpenAI
import os

def get_llm():
    return ChatOpenAI(
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )

from transformers import pipeline

def get_llm():
    return pipeline("text-generation", model="google/flan-t5-base")

def generate_answer(llm, context, query):
    prompt = f"""
    Answer based only on context:

    {context}

    Question: {query}
    """

    response = llm(prompt, max_length=256)
    return response[0]['generated_text']