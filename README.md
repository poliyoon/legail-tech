# Legal AI Studio | 전문 법률 자문 AI

법률 도메인에 특화된 고성능 AI 자문 서비스입니다. RAG(Retrieval-Augmented Generation) 기술을 활용하여 방대한 법률 데이터를 분석하고 정확한 조언을 제공합니다.

## ✨ 주요 기능
- **전문 법률 지식 기반 답변**: 민사, 형사, 근로기준법 등 다양한 법률 데이터 학습
- **대화형 웹 인터페이스**: 다크 모드 기반의 프리미엄 디자인
- **RAG 시스템**: 관련 법률 문서를 실시간으로 검색하여 근거 있는 답변 생성

## 🛠 기술 스택
- **Backend**: FastAPI (Python)
- **Frontend**: Vanilla JS, Vanilla CSS
- **AI/LLM**: OpenAI GPT-4o-mini
- **Vector DB**: FAISS (with OpenAI Embeddings)
- **Deployment**: Vercel

## 🚀 시작하기

### 1. 환경 설정
`.env` 파일을 생성하고 OpenAI API 키를 입력하세요:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 2. 실행 방법 (로컬)
```bash
pip install -r requirements.txt
python main.py
```
접속 주소: `http://127.0.0.1:8001`

## 📦 배포 방법 (Vercel)
1. GitHub 저장소에 코드를 업로드합니다.
2. Vercel 콘솔에서 프로젝트를 연결합니다.
3. Environment Variables에 `OPENAI_API_KEY`를 추가합니다.

---
&copy; 2026 Legal AI Studio
