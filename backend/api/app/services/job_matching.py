from typing import List, Dict, Any, Optional
from .llm_service import llm_service

class JobMatchingService:
    """Service for matching jobs to user profiles"""
    
    def __init__(self):
        """Initialize the job matching service"""
        pass
    
    def match_jobs_to_profile(self, profile_data: Dict[str, Any], jobs: List[Dict[str, Any]], 
                              min_score: float = 0.0, limit: int = 10) -> List[Dict[str, Any]]:
        """Match jobs to a user profile and return sorted by match score"""
        
        jobs_with_scores = []
        for job in jobs:
            match_score = llm_service.calculate_job_match_score(profile_data, job)
            job_with_score = job.copy()
            job_with_score["match_score"] = match_score
            jobs_with_scores.append(job_with_score)
        
        filtered_jobs = [job for job in jobs_with_scores if job["match_score"] >= min_score]
        
        sorted_jobs = sorted(filtered_jobs, key=lambda x: x["match_score"], reverse=True)
        
        limited_jobs = sorted_jobs[:limit]
        
        return limited_jobs
    
    def get_top_matching_jobs(self, profile_data: Dict[str, Any], jobs: List[Dict[str, Any]], 
                             limit: int = 10) -> List[Dict[str, Any]]:
        """Get top matching jobs for a user profile"""
        return self.match_jobs_to_profile(profile_data, jobs, min_score=0.0, limit=limit)

job_matching_service = JobMatchingService()
