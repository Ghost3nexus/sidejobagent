from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from ..schemas.user import UserCreate, UserResponse, Token
from ..utils.auth import (
    verify_password, 
    get_password_hash, 
    create_access_token, 
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from ..utils.db import db
from ..config import SECRET_KEY

router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post("/register", response_model=Token)
async def register(user_data: UserCreate):
    existing_user = db.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    hashed_password = get_password_hash(user_data.password)
    user_dict = user_data.dict()
    user_dict.pop("password")
    user_dict["hashed_password"] = hashed_password
    
    created_user = db.create_user(user_dict)
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": created_user["id"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get_user_by_email(form_data.username)  # username is email in this case
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["id"]}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
