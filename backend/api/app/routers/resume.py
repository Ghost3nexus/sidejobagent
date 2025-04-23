from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, Optional

from ..schemas.user import UserResponse
from ..schemas.job import JobResponse
from ..utils.auth import get_current_user
from ..utils.db import db
from ..services.resume_builder import resume_builder_service

router = APIRouter(prefix="/resume", tags=["resume"])

@router.post("/generate")
async def generate_resume(
    job_id: Optional[str] = None,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    """Generate a resume based on user profile and optionally a specific job"""
    
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Please create a profile first."
        )
    
    job_data = None
    if job_id:
        job = db.get_job_by_id(job_id)
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )
        job_data = job
    
    resume_content = resume_builder_service.generate_resume(profile, job_data)
    
    return {
        "content": resume_content,
        "format": "markdown"
    }

@router.post("/generate-html")
async def generate_resume_html(
    job_id: Optional[str] = None,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    """Generate a resume in HTML format based on user profile and optionally a specific job"""
    
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Please create a profile first."
        )
    
    job_data = None
    if job_id:
        job = db.get_job_by_id(job_id)
        if not job:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Job not found"
            )
        job_data = job
    
    resume_markdown = resume_builder_service.generate_resume(profile, job_data)
    resume_html = resume_builder_service.format_resume_as_html(resume_markdown)
    
    return {
        "content": resume_html,
        "format": "html"
    }
