from fastapi import APIRouter , HTTPException , Depends
from pydantic import BaseModel
from app_backend.schemas.chat import ChatResponse , ChatRequest
from app_backend.services.chat_service import process_chat
from app_backend.core.rate_limiter import check_rate_limit

router = APIRouter()


# #request body schema
# class ChatRequest(BaseModel):
#     question:str

# #Response schema
# class ChatResponse(BaseModel):
#     answer:str
#     disclaimer:str

@router.post("/chat", response_model=ChatResponse)
def chat_with_medical_ai(request: ChatRequest , user_id:str="demo-user"):
    if not check_rate_limit(user_id):
        raise HTTPException(status_code=429 ,detail="Too many requets")
    return process_chat(request , user_id)




