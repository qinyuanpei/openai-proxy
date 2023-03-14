
from pydantic import BaseModel
from typing import List

class MessageModel(BaseModel):
    role: str
    content: str

class RequestModel(BaseModel):
    model: str = "gpt-3.5-turbo"
    messages: List[MessageModel] = []