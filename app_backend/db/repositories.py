from app_backend.db.mongo import chat_collection
from datetime import datetime
from app_backend.db.mongo import db

def save_chat(question: str, answer: str):
    document = {
        "question": question,
        "answer": answer,
        "created_at": datetime.utcnow()
    }
    chat_collection.insert_one(document)


def get_all_chats():
    chats = []
    for chat in chat_collection.find({}, {"_id": 0}):
        chats.append(chat)
    return chats


soap_collection = db["soap_reports"]

def save_soap_report(report:dict):
    return soap_collection.insert_one(report)