from fastapi import FastAPI, Header, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
import openai

class MessageModel(BaseModel):
    role: str
    content: str

class RequestModel(BaseModel):
    model: str
    messages: List[MessageModel]

app = FastAPI()

@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI.", "timestamp": datetime.now()}

@app.post("/openai/v1/completions")
def do_proxy(request: RequestModel, authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        openai.api_key = authorization.replace("Bearer", "").strip()
        completion = openai.ChatCompletion.create(model=request.model, messages=request.messages)
        return completion
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="")
    