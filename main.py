import os
from typing import List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from groq import Groq

load_dotenv()

API_KEY = os.getenv("RAG")
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")
KNOWLEDGE_FILE = "sample_docs/knowledge.txt"

app = FastAPI(title="AI & RAG Assistant")

# Configure templates directory
templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Schemas
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    mode: str  # "basic" or "rag"
    message: str
    history: Optional[List[Message]] = []

class ChatResponse(BaseModel):
    reply: str

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="GROQ_API_KEY is not set in environment variables.")

    try:
        client = Groq(api_key=API_KEY)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to initialize Groq client: {str(e)}")

    if request.mode == "basic":
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        for msg in request.history:
            messages.append({"role": msg.role, "content": msg.content})
        messages.append({"role": "user", "content": request.message})

        try:
            response = client.chat.completions.create(messages=messages, model=MODEL)
            reply = response.choices[0].message.content
            return ChatResponse(reply=reply)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")

    elif request.mode == "rag":
        if not os.path.exists(KNOWLEDGE_FILE):
            raise HTTPException(status_code=404, detail=f"Knowledge base file '{KNOWLEDGE_FILE}' not found.")

        try:
            with open(KNOWLEDGE_FILE, encoding="utf-8") as file:
                document = file.read()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading knowledge file: {str(e)}")

        rag_messages = [
            {"role": "system", "content": "Answer using only the document below."},
            {
                "role": "user",
                "content": f"Document:\n{document}\n\nQuestion: {request.message}",
            },
        ]

        try:
            response = client.chat.completions.create(messages=rag_messages, model=MODEL)
            reply = response.choices[0].message.content
            return ChatResponse(reply=reply)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")

    else:
        raise HTTPException(status_code=400, detail="Invalid mode selected. Use 'basic' or 'rag'.")
    
    print("fastapi done")