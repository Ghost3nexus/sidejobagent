from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any, Optional

from ..schemas.job import JobResponse, ApplicationCreate, ApplicationResponse, JobWithMatchScore
from ..utils.auth import get_current_user
from ..utils.db import db

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.get("/jobs", response_model=List[JobResponse])
async def get_jobs(
    limit: int = 10,
    offset: int = 0,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    all_jobs = db.get_all_jobs()
    return all_jobs[offset:offset+limit]

@router.get("/jobs/{job_id}", response_model=JobResponse)
async def get_job(
    job_id: str,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    job = db.get_job_by_id(job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    return job

@router.get("/jobs/match", response_model=List[JobWithMatchScore])
async def get_matched_jobs(
    limit: int = 10,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    profile = db.get_profile_by_user_id(current_user["id"])
    if not profile:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Profile not found, please create a profile first"
        )
    
    all_jobs = db.get_all_jobs()
    matched_jobs = []
    
    for job in all_jobs:
        user_skills = set(profile.get("skills", []))
        job_skills = set(job.get("skills", []))
        
        if not user_skills or not job_skills:
            match_score = 0.0
        else:
            common_skills = user_skills.intersection(job_skills)
            match_score = len(common_skills) / max(len(user_skills), len(job_skills))
        
        job_with_score = {**job, "match_score": match_score}
        matched_jobs.append(job_with_score)
    
    matched_jobs.sort(key=lambda x: x["match_score"], reverse=True)
    
    return matched_jobs[:limit]

@router.post("/jobs/{job_id}/apply", response_model=ApplicationResponse)
async def apply_to_job(
    job_id: str,
    application_data: ApplicationCreate,
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    job = db.get_job_by_id(job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    application_dict = application_data.dict()
    application_dict["user_id"] = current_user["id"]
    application_dict["job_id"] = job_id
    
    created_application = db.create_application(application_dict)
    return created_application

@router.get("/applications", response_model=List[ApplicationResponse])
async def get_user_applications(
    current_user: Dict[str, Any] = Depends(get_current_user)
):
    applications = db.get_applications_by_user_id(current_user["id"])
    return applications
