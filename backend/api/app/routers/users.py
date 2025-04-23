from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any

from ..schemas.user import UserResponse, ProfileCreate, ProfileUpdate, ProfileResponse
from ..utils.auth import get_current_user
from ..utils.db import db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(current_user: Dict[str, Any] = Depends(get_current_user)):
    return current_user

@router.get("/profile", response_model=ProfileResponse)
async def get_user_profile(current_user: Dict[str, Any] = Depends(get_current_user)):
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    return profile

@router.post("/profile", response_model=ProfileResponse)
async def create_user_profile(
    profile_data: ProfileCreate,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    existing_profile = db.get_profile_by_user_id(current_user["id"])
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile already exists"
        )
    
    profile_dict = profile_data.dict()
    profile_dict["user_id"] = current_user["id"]
    
    created_profile = db.create_profile(profile_dict)
    return created_profile

@router.put("/profile", response_model=ProfileResponse)
async def update_user_profile(
    profile_data: ProfileUpdate,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    existing_profile = db.get_profile_by_user_id(current_user["id"])
    if not existing_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found"
        )
    
    updated_profile = db.update_profile(existing_profile["id"], profile_data.dict())
    return updated_profile
