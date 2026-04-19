import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from groq import Groq
load_dotenv()

class ChatRequest(BaseModel):
    message: str
    temperature: float = 0.7

class ChatResponse(BaseModel):
    response: str
    temperature_used:float


@app.get("/")
def read_root():
    return {"App is Running Successfully!"}


@app.post("/chat")

def read_item(request: ChatRequest):
    try:
        client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="llama-3.3-70b-versatile",
            temperature=request.temperature
        )

        return ChatResponse(
            response=chat_completion.choices[0].message.content,
            temperature_used=request.temperature
        )
    except Exception as e:
        return {"error": str(e)}