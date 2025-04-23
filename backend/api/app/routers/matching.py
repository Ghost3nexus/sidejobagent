from fastapi import APIRouter, Depends, HTTPException, status
from typing import Dict, Any, List, Optional

from ..schemas.user import UserResponse
from ..schemas.job import JobWithMatchScore
from ..utils.auth import get_current_user
from ..utils.db import db
from ..services.job_matching import job_matching_service
from ..services.scraper import job_scraper

router = APIRouter(prefix="/matching", tags=["matching"])

@router.get("")
async def get_matching_jobs(
    min_score: float = 0.0,
    limit: int = 10,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    """Get jobs matching the user's profile"""
    
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found. Please create a profile first."
        )
    
    jobs = db.get_all_jobs()
    
    if not jobs:
        jobs = job_scraper.fetch_mock_jobs()
    
    matched_jobs = job_matching_service.match_jobs_to_profile(
        profile, jobs, min_score=min_score, limit=limit
    )
    
    return matched_jobs
