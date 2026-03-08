from langchain_ollama import OllamaLLM,OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

llm = OllamaLLM(model="llama3.2:3b")

embeddings = OllamaEmbeddings(model="llama3.2:3b")

index_name = os.getenv("PINECONE_INDEX_NAME")

store = {}


def get_vectorstore():
    return PineconeVectorStore(index_name=index_name,embedding=embeddings)

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are Nexus v2. Use the provided context to answer. If you don't know, say so."),
    MessagesPlaceholder(variable_name="history"),
    ("system", "Context: {context}"),
    ("human", "{question}"),
])

chain = prompt | llm

brain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

def search_and_answer(question, session_id="user_1"):
    vectorstore = get_vectorstore()
    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])
    
    return brain_with_history.invoke(
        {"question": question, "context": context},
        config={"configurable": {"session_id": session_id}}
    )