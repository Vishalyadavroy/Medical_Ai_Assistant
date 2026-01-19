from fastapi import APIRouter, HTTPException
from app_backend.schemas.auth  import UserCreate , UserLogin , TokenResponse
from app_backend.services.auth_service import create_user, authenticate_user ,create_access_token




router = APIRouter(prefix="/auth" ,tags=["Auth"])
router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/register")
def register(user:UserCreate):
    create_user(user.email, user.password)
    return {"message":"User registered"}

@router.post("/login" , response_model=TokenResponse)
def login(user:UserLogin):
    if not authenticate_user(user.email , user.password):
        raise HTTPException(status_code=401 , details="Invalid credentails")
    
    token = create_access_token(user.email)
    return {"access_token":token}


