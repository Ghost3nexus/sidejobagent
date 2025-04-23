from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any

from ..schemas.user import UserResponse
from ..schemas.job import JobResponse
from ..utils.auth import get_current_user
from ..utils.db import db
from ..services.resume_builder import resume_builder_service

router = APIRouter(prefix="/cover-letter", tags=["cover-letter"])

@router.post("")
async def generate_cover_letter(
    job_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    """Generate a cover letter based on user profile and a specific job"""
    
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Please create a profile first."
        )
    
    job = db.get_job_by_id(job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    cover_letter_content = resume_builder_service.generate_cover_letter(profile, job)
    
    return {
        "content": cover_letter_content,
        "format": "markdown"
    }
