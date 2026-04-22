import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

from groq import Groq

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading .env file: {e}")

# Validate API key at startup
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY environment variable is not set. "
        "Please set it in Railway dashboard or .env file"
    )

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
        api_key=GROQ_API_KEY,
    )

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=request.temperature
        )

        return ChatResponse(
            response=chat_completion.choices[0].message.content,
            temperature_used=request.temperature
        )
    except Exception as e:
        return {"error": str(e)}
    
if __name__ == "__main__":
    import uvicorn
    
    # Step 1: Get port from environment
    port = os.getenv("PORT", "8000")
    
    # Step 2: YOUR TASK - Convert port to integer
    # Hint: What function converts strings to integers?
    
    # Step 3: Start the server
    uvicorn.run("main:app", host="0.0.0.0", port=int(port))  # Fill in the ???