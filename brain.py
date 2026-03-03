from langchain_ollama import OllamaLLM
from langchain_community.embeddings import OllamaEmbeddings

llm = OllamaLLM(model="llama3.2:3b")

embeddings = OllamaEmbeddings(model="llama3.2:3b")

def ask_nexus(question, context=""):
    prompt = f"""
    You are Nexus v2, an Advanced AI Assistant.
    Use the following context to answer the user's question.
    If the context is empty, answer based on your general knowledge.
    
    Context: {context}
    User Question: {question}
    
    Answer:
    """
    return llm.invoke(prompt)