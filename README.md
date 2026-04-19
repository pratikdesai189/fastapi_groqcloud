# Fast Api with GroqCloud

## 1. llama-3.3-70b-versatile chat App

This project uses the open source model llama-3.3-70b-versatile from the groq and works as a chat bot that gives answers from the user input

## 2. Feature

It takes input from the user in Fast Api and writes response to it

## 3. Tech Stack

- Python
- Fast Api
- Groq Cloud Api
- dot env

## 4. Setup Instructions

clone the repository in local
`pip install -r requirement.txt`

## 5. API Endpoint

/chat 

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

## 6. Learning

I learned how to use open source models and create chat bot that runs on this model for free using the API key i learned the .env operations i learned the fast api how to integrate groq api call inside it 

