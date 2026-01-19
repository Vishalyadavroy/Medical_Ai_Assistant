from app_backend.db.mongo import chat_collection
from datetime import datetime
from app_backend.db.mongo import db

def save_chat(user_id:str, question: str, answer: str):
    document = {
        "user_id":user_id,
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


def get_user_chats(user_id: str):
    return list(chat_collection.find(
        {"user_id": user_id},
        {"_id": 0}
    ))


soap_collection = db["soap_reports"]

def save_soap_report(report:dict):
    return soap_collection.insert_one(report)


def get_all_chats(user_id: str):
    return list(chat_collection.find({"user_id": user_id}))


def save_soap_report(data: dict):
    soap_collection.insert_one(data)
