#  AI Personal Assistant using Python & LLM

An AI-powered conversational personal assistant built using **Python, LangChain, Groq LLM, FastAPI, HTML, CSS, and JavaScript**.

The application provides context-aware question answering, conversation memory, prompt-engineered responses, and interactive assistance for studying, planning, programming, and idea generation.

##  Live Demo

 **Live Application:**  
https://ai-personal-assistant-olive.vercel.app

 **GitHub Repository:**  
https://github.com/Aish-26-C/AI-Personal-Assistant

---

##  Features

-  AI-powered conversational chat
- Conversation memory
-  Context-aware question answering
-  Groq LLM integration
- LangChain integration
-  Prompt engineering
-  Study assistance
-  Task and project planning
-  Programming assistance
-  AI-powered idea generation
-  Clear conversation memory
- Interactive and colourful web interface
-  FastAPI backend
-  Deployed using Vercel

---

## System Architecture

```text
                    USER
                       │
                       ▼
              ┌─────────────────┐
              │   Web Interface │
              │  HTML/CSS/JS    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     FastAPI     │
              │    REST API     │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    LangChain    │
              │                 │
              │ Prompt + Memory │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │    Groq LLM     │
              │  Llama Model    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │   AI Response   │
              └────────┬────────┘
                       │
                       ▼
                  👤 USER
