from fastapi import FastAPI, Header, HTTPException
from typing import List, Optional
from pydantic import BaseModel
import openai

class MessageModel(BaseModel):
    role: str
    content: str

class RequestModel(BaseModel):
    model: str
    messages: List[MessageModel]
    max_tokens: int
    temperature: float
    frequency_penalty: float
    presence_penalty: float

app = FastAPI()

@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI."}

@app.post("/openai/v1/completions")
def do_proxy(request: RequestModel, authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    openai.api_key = authorization.replace("Bearer", "").strip()
    completion = openai.ChatCompletion.create()
    return completion
    