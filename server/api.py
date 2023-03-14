from fastapi import FastAPI, Header, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import Optional
from datetime import datetime
import openai
import logging

from models import RequestModel
from utils import resp_200

app = FastAPI()

@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI.", "timestamp": datetime.now()}

@app.post("/openai/v1/completions")
def do_proxy(request: RequestModel, authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        request = jsonable_encoder(request)
        openai.api_key = authorization.replace("Bearer", "").strip()
        completion = openai.ChatCompletion.create(model=request['model'], messages=request['messages'])
        return resp_200(data=completion)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="")
    