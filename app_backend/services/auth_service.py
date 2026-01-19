from passlib.context import CryptContext
from jose import jwt 
from datetime import datetime, timedelta
import os 

SECRET_KEY = os.getenv("SECRET_KEY" , "secret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users_db ={}

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password:str , hashed:str):
    return pwd_context.verify(password ,hashed)

def  create_user(email:str, password:str):
    users_db[email]= hash_password(password)

def authenticate_user(email:str, password:str):
    if email not in users_db:
        return False
    return verify_password(password , users_db[email])

def create_access_token(email:str):
    payload ={
        "sub":email,
        "exp":datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return jwt.encode(payload ,SECRET_KEY , algorithm=ALGORITHM)