from pydantic import BaseModel
from typing import List, Optional

class JobBase(BaseModel):
    title: str
    description: str
    url: str
    source: str
    compensation: str
    skills: List[str]

class JobCreate(JobBase):
    pass

class JobResponse(JobBase):
    id: str
    created_at: str

    class Config:
        from_attributes = True

class ApplicationBase(BaseModel):
    job_id: str
    cover_letter: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: str
    user_id: str
    status: str
    created_at: str

    class Config:
        from_attributes = True

class JobWithMatchScore(JobResponse):
    match_score: float
