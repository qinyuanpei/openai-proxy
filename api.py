from fastapi import FastAPI, Header, HTTPException, File
from typing import Optional
from datetime import datetime
import openai
import logging

from utils import resp_200

app = FastAPI()

@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI.", "timestamp": datetime.now()}

@app.post("/v1/completions")
def do_proxy_chat(request: dict, authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        openai.api_key = authorization.replace("Bearer", "").strip()
        completion = openai.ChatCompletion.create(model=request['model'], messages=request['messages'])
        return resp_200(data=completion)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="")

@app.post("/v1/audio/transcriptions")   
def do_proxy_whisper(file: bytes = File(..., max_length=10485760), authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        transcript = openai.Audio.transcribe("whisper-1", file)
        return resp_200(data=transcript)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="")
    