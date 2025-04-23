from typing import Dict, List, Optional, Any
import uuid
from datetime import datetime

class InMemoryDB:
    """
    In-memory database for development purposes.
    This simulates a database with tables for users, profiles, and jobs.
    """
    def __init__(self):
        self.users: Dict[str, Dict[str, Any]] = {}
        self.profiles: Dict[str, Dict[str, Any]] = {}
        self.jobs: Dict[str, Dict[str, Any]] = {}
        self.applications: Dict[str, Dict[str, Any]] = {}
        
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new user"""
        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "email": user_data.get("email"),
            "username": user_data.get("username"),
            "hashed_password": user_data.get("hashed_password"),
            "created_at": datetime.now().isoformat(),
        }
        self.users[user_id] = user
        return user
    
    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user by ID"""
        return self.users.get(user_id)
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email"""
        for user in self.users.values():
            if user["email"] == email:
                return user
        return None
    
    def create_profile(self, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new profile for a user"""
        profile_id = str(uuid.uuid4())
        profile = {
            "id": profile_id,
            "user_id": profile_data.get("user_id"),
            "job_type": profile_data.get("job_type", ""),
            "skills": profile_data.get("skills", []),
            "desired_compensation": profile_data.get("desired_compensation", ""),
            "work_hours": profile_data.get("work_hours", ""),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        self.profiles[profile_id] = profile
        return profile
    
    def get_profile_by_user_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get profile by user ID"""
        for profile in self.profiles.values():
            if profile["user_id"] == user_id:
                return profile
        return None
    
    def update_profile(self, profile_id: str, profile_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an existing profile"""
        if profile_id not in self.profiles:
            return None
        
        profile = self.profiles[profile_id]
        for key, value in profile_data.items():
            if key != "id" and key != "user_id" and key != "created_at":
                profile[key] = value
        
        profile["updated_at"] = datetime.now().isoformat()
        return profile
    
    def create_job(self, job_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new job listing"""
        job_id = str(uuid.uuid4())
        job = {
            "id": job_id,
            "title": job_data.get("title", ""),
            "description": job_data.get("description", ""),
            "url": job_data.get("url", ""),
            "source": job_data.get("source", ""),
            "compensation": job_data.get("compensation", ""),
            "skills": job_data.get("skills", []),
            "created_at": datetime.now().isoformat(),
        }
        self.jobs[job_id] = job
        return job
    
    def get_job_by_id(self, job_id: str) -> Optional[Dict[str, Any]]:
        """Get job by ID"""
        return self.jobs.get(job_id)
    
    def get_all_jobs(self) -> List[Dict[str, Any]]:
        """Get all jobs"""
        return list(self.jobs.values())
    
    def create_application(self, application_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new job application"""
        application_id = str(uuid.uuid4())
        application = {
            "id": application_id,
            "user_id": application_data.get("user_id"),
            "job_id": application_data.get("job_id"),
            "status": application_data.get("status", "applied"),
            "cover_letter": application_data.get("cover_letter", ""),
            "created_at": datetime.now().isoformat(),
        }
        self.applications[application_id] = application
        return application
    
    def get_applications_by_user_id(self, user_id: str) -> List[Dict[str, Any]]:
        """Get all applications for a user"""
        return [app for app in self.applications.values() if app["user_id"] == user_id]

db = InMemoryDB()
