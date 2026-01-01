"""
models/legal_advisor_model.py
Manual RAG Implementation (Bypasses langchain.chains).
Created: 2026-01-01T11:40:00+09:00
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from data.legal_docs import get_all_docs

load_dotenv()

class LegalAdvisorModel:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        
        # Initialize Embeddings (OpenAI for lightweight Vercel deployment)
        self.embeddings = OpenAIEmbeddings(api_key=self.api_key)
        
        # Initialize LLM
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            api_key=self.api_key,
            temperature=0
        )
        
        self.vector_store = self._initialize_vector_store()

    def _initialize_vector_store(self):
        docs = get_all_docs()
        texts = [doc["content"] for doc in docs]
        metadatas = [{"title": doc["title"], "category": doc["category"]} for doc in docs]
        
        vector_store = FAISS.from_texts(texts, self.embeddings, metadatas=metadatas)
        return vector_store

    def get_advice(self, query: str):
        # 1. Manual Retrieval
        # Retrieve top 3 relevant documents
        docs = self.vector_store.similarity_search(query, k=3)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # 2. Manual Prompting
        system_prompt = (
            "당신은 전문 법률 자문 AI입니다. 아래 제공된 법률 정보(Context)를 바탕으로 사용자의 질문에 답변하세요.\n"
            "정보가 충분하지 않다면 아는 범위 내에서 조언하되, 반드시 법률 전문가와 상담할 것을 권고하세요.\n"
            "답변은 친절하고 전문적인 용어를 사용하여 논리적으로 구성하세요."
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "Context:\n{context}\n\nQuestion: {question}")
        ])
        
        # 3. Direct Invocation
        chain = prompt | self.llm
        response = chain.invoke({"context": context, "question": query})
        
        return response.content

# Singleton instance
legal_model = None

def get_legal_model():
    global legal_model
    if legal_model is None:
        legal_model = LegalAdvisorModel()
    return legal_model
