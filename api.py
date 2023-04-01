from fastapi import FastAPI, Header, HTTPException, File, UploadFile
from typing import Optional
from datetime import datetime
import openai
import logging
import os
from io import BytesIO

from utils import resp_200

app = FastAPI()


@app.get("/")
def do_echo():
    return {"message": "This is a greet from FastAPI.", "timestamp": datetime.now()}

@app.post("/v1/chat/completions")
async def do_proxy_chat(request: dict, authorization: Optional[str] = Header(None)):
    # if (authorization == None):
    #     raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
    try:
        # openai.api_key = authorization.replace("Bearer", "").strip()
        # completion = openai.ChatCompletion.create(model=request['model'], messages=request['messages'])
        openai.api_key = os.environ.get("OPENAI_API_KEY")  # �ӻ��������ж�ȡAPI_KEY
        completions = openai.Completion.create(
            # prompt      = request['prompt'],
            engine      = request['model'] if request['model'] is None else 'gpt-3.5-turbo',
            temperature = request['temperature'] if request['temperature'] is None else 0.7,
            max_tokens  = 1024,
            prompt = request['prompt']
        )

        completion = completions.choices[0].text

        return resp_200(data=completion)
    except Exception as e:
        logging.error(e)
        raise HTTPException(status_code=500, detail="")

# @app.post("/v1/audio/transcriptions")   
# async def do_proxy_whisper(file: UploadFile, authorization: Optional[str] = Header(None)):
#     if (authorization == None):
#         raise HTTPException(status_code=401, detail="OPENAI_API_KEY is required.")
    
#     try:
#         openai.api_key = authorization.replace("Bearer", "").strip()
#         contents = await file.read()
#         audio = openai.Audio(BytesIO(contents))
#         transcript = openai.Audio.transcribe("whisper-1", audio)
#         return resp_200(data=transcript)
#     except Exception as e:
#         logging.error(e)
#         raise HTTPException(status_code=500, detail="")
    