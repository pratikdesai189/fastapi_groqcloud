# Fast Api with GroqCloud

## 1. llama-3.3-70b-versatile chat App

This project uses the open source model llama-3.3-70b-versatile from the groq and works as a chat bot that gives answers from the user input

## 2. Feature

- Chat with LLM using natural language
- Adjustable temperature (0.1-2.0) for response creativity
- Returns both response and temperature used
- Error handling for API failures
- FastAPI automatic documentation (Swagger UI)

## 3. Tech Stack

- Python
- Fast Api
- Groq Cloud Api
- dot env

## 4. Setup Instructions

clone the repository in local
`pip install -r requirement.txt`

go to groq cloud and create your own API key
create .env file and add your api key there ex. GROQ_API_KEY=<Your Api Key Here>

`uvicorn main:app --reload` to run the server and autoreaload when you do some changes

Open browser and go to `http://localhost:8000/docs` to test the API

## 5. API Endpoint

/chat : this accepts string input

### POST /chat

Send a message to the LLM and get a response.

**Request:**
```json
{
  "message": "Who is Dr. Abdul Kalam?",
  "temperature": 0.7
}
```

**Response:**
```json
{
  "response": "Dr. Abdul Kalam was...",
  "temperature_used": 0.7
}
```
## 6 Requirements
```
fastapi
uvicorn
python-dotenv
groq
```

## 7. Learning

- How to integrate open-source LLM models using Groq API
- FastAPI endpoint creation and request/response handling
- Environment variable management with python-dotenv
- Pydantic models for request/response validation
- Error handling in API development

