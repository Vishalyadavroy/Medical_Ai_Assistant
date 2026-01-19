# from app_backend.db.repositories import get_all_chats ,save_soap_report
# from app_backend.services.ai_service import generate_medical_answer
# from datetime import datetime

# def generate_soap_report(user_id:str) -> str:
#     chats = get_all_chats(user_id)

#     if not chats:
#         return "No conversation data available to generate SOAP report."

#     conversation_text = ""
#     for chat in chats:
#         conversation_text += f"User: {chat['question']}\nAI: {chat['answer']}\n\n"

#     soap_prompt = f"""
# Based on the following medical conversation, generate a SOAP report.

# RULES:
# - Do NOT diagnose
# - Do NOT prescribe medications
# - Use neutral and professional language
# - Assessment must be observational, not diagnostic
# - Plan should suggest general education and professional consultation

# Conversation:
# {conversation_text}

# Format strictly as:
# S:
# O:
# A:
# P:
# """
#     soap_report = generate_medical_answer(soap_prompt)

#     save_soap_report({
#         "report":soap_report,
#         "creted_at":datetime.utcnow()
#     })

#     return generate_medical_answer(soap_prompt)


from app_backend.db.repositories import get_all_chats, save_soap_report
from app_backend.services.ai_service import generate_medical_answer
from datetime import datetime


def generate_soap_report(user_id: str) -> str:
    # 1. Fetch chats for this user
    chats = get_all_chats(user_id)

    if not chats:
        return "No conversation data available to generate SOAP report."

    # 2. Build conversation text
    conversation_text = ""
    for chat in chats:
        conversation_text += f"User: {chat['question']}\nAI: {chat['answer']}\n\n"

    # 3. Build SOAP prompt
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

    # 4. Generate SOAP report (ONLY ONCE)
    soap_report = generate_medical_answer(soap_prompt)

    # 5. Save SOAP report
    save_soap_report({
        "user_id": user_id,
        "report": soap_report,
        "created_at": datetime.utcnow()
    })

    # 6. Return the same report
    return soap_report
