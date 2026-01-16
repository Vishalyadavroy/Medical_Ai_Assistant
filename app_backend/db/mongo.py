from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # 🔥 THIS LINE IS REQUIRED

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in .env file")

client = MongoClient(MONGO_URL)

db = client["medical_ai_db"]
chat_collection = db["chats"]
