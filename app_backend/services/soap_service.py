from app_backend.db.repositories import get_all_chats ,save_soap_report
from app_backend.services.ai_service import generate_medical_answer
from datetime import datetime
def generate_soap_report() -> str:
    chats = get_all_chats()

    if not chats:
        return "No conversation data available to generate SOAP report."

    conversation_text = ""
    for chat in chats:
        conversation_text += f"User: {chat['question']}\nAI: {chat['answer']}\n\n"

    soap_prompt = f"""
Based on the following medical conversation, generate a SOAP report.

RULES:
- Do NOT diagnose
- Do NOT prescribe medications
- Use neutral and professional language
- Assessment must be observational, not diagnostic
- Plan should suggest general education and professional consultation

Conversation:
{conversation_text}

Format strictly as:
S:
O:
A:
P:
"""
    soap_report = generate_medical_answer(soap_prompt)

    save_soap_report({
        "report":soap_report,
        "creted_at":datetime.utcnow()
    })

    return generate_medical_answer(soap_prompt)
