from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

from backend.chatbot import (
    get_ai_response,
    clear_conversation
)


app = FastAPI(
    title="AI Personal Assistant",
    description="AI-powered conversational assistant",
    version="1.0.0"
)


# =========================================
# CORS
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# =========================================
# REQUEST MODEL
# =========================================

class ChatRequest(BaseModel):
    message: str


# =========================================
# FRONTEND
# =========================================

app.mount(
    "/frontend",
    StaticFiles(directory="frontend"),
    name="frontend"
)


@app.get("/")
def home():
    return FileResponse(
        "frontend/index.html"
    )


# =========================================
# CHAT API
# =========================================

@app.post("/chat")
def chat(request: ChatRequest):

    response = get_ai_response(
        request.message
    )

    return {
        "response": response
    }


# =========================================
# CLEAR MEMORY API
# =========================================

@app.post("/clear")
def clear_chat():

    clear_conversation()

    return {
        "message":
        "Conversation memory cleared successfully."
    }