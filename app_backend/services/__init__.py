from pydantic import BaseModel


class ChatRequest(BaseModel):
    question:str


class ChatResponse(BaseModel):
    asnwer: str
    disclaimer: str