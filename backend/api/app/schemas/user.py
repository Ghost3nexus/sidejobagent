from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: str
    created_at: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[str] = None

class ProfileBase(BaseModel):
    job_type: Optional[str] = None
    skills: Optional[List[str]] = None
    desired_compensation: Optional[str] = None
    work_hours: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileResponse(ProfileBase):
    id: str
    user_id: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True
