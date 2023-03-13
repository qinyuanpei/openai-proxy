from fastapi import FastAPI, Header, HTTPException, status
from fastapi.responses import JSONResponse, Response  
from fastapi.encoders import jsonable_encoder
from typing import List, Optional, Union
from pydantic import BaseModel
from datetime import datetime
import openai

class MessageModel(BaseModel):
    role: str
    content: str

class RequestModel(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: List[MessageModel] = []

app = FastAPI()

@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI.", "timestamp": datetime.now()}

def resp_200(*, data: Union[list, dict, str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': "Success",
            'data': data,
        }
    )  

@app.post("/openai/v1/completions")
def do_proxy(request: RequestModel, authorization: Optional[str] = Header(None)):
    if (authorization == None):
        raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        request = jsonable_encoder(request)
        openai.api_key = authorization.replace("Bearer", "").strip()
        completion = openai.ChatCompletion.create(model=request.model, messages=request.messages)
        return resp_200(data=completion)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="")
    