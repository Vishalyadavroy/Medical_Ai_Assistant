from app_backend.schemas.chat import ChatRequest, ChatResponse
from app_backend.db.repositories import save_chat
from app_backend.services.ai_service import generate_medical_answer

def process_chat(request: ChatRequest) -> ChatResponse:
    answer = generate_medical_answer(request.question)
    

    
    save_chat(
        question=request.question,
        answer=answer
    )

    return ChatResponse(
        answer=answer,
        disclaimer="This information is for educational purposes only and is not a substitute for professional medical advice."
    )
