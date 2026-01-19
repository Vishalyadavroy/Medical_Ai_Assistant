from app_backend.schemas.chat import ChatRequest, ChatResponse
from app_backend.db.repositories import save_chat
from app_backend.services.ai_service import generate_medical_answer
from app_backend.core.medical_filter import ( is_critical_medical_query, EMERGENCY_RESPONSE)




def process_chat(request: ChatRequest, user_id: str) -> ChatResponse:
    

    if is_critical_medical_query(request.question):
        save_chat(
            user_id=user_id,
            question=request.question,
            answer=EMERGENCY_RESPONSE  # ✅ FIXED
        )

        return ChatResponse(
            answer=EMERGENCY_RESPONSE,
            disclaimer="Emergency guidance only. Not a diagnosis."
        )
    
    print("QUESTION RECEIVED:", request.question)
    print("IS CRITICAL:", is_critical_medical_query(request.question))

    answer = generate_medical_answer(request.question)

    save_chat(
        user_id=user_id,
        question=request.question,
        answer=answer
    )

    return ChatResponse(
        answer=answer,
        disclaimer="Educational information only."
    )

