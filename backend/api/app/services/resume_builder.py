from typing import Dict, Any, Optional
from .llm_service import llm_service
import os
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class ResumeBuilderService:
    """Service for building resumes"""
    
    def __init__(self):
        """Initialize the resume builder service"""
        pass
    
    def generate_resume(self, profile_data: Dict[str, Any], job_data: Optional[Dict[str, Any]] = None) -> str:
        """Generate a resume based on profile data and optionally job data"""
        return llm_service.generate_resume(profile_data, job_data)
    
    def generate_cover_letter(self, profile_data: Dict[str, Any], job_data: Dict[str, Any]) -> str:
        """Generate a cover letter based on profile data and job data"""
        return llm_service.generate_cover_letter(profile_data, job_data)
    
    def format_resume_as_html(self, resume_markdown: str) -> str:
        """Format a resume in markdown as HTML"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>職務経歴書</title>
            <style>
                body {{
                    font-family: 'Helvetica Neue', Arial, sans-serif;
                    line-height: 1.6;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }}
                h1, h2, h3 {{
                    color: #333;
                }}
                h1 {{
                    text-align: center;
                    border-bottom: 2px solid #333;
                    padding-bottom: 10px;
                }}
                h2 {{
                    border-bottom: 1px solid #ddd;
                    padding-bottom: 5px;
                    margin-top: 30px;
                }}
                ul {{
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="resume-content">
                {resume_markdown.replace('\n', '<br>')}
            </div>
        </body>
        </html>
        """
        return html
    
    def save_resume_to_file(self, resume_content: str, format_type: str = "markdown") -> str:
        """Save resume content to a file and return the file path"""
        
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"resume_{timestamp}.{format_type}"
        file_path = f"/tmp/{filename}"
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(resume_content)
            return file_path
        except Exception as e:
            logger.error(f"Error saving resume to file: {str(e)}")
            return ""

resume_builder_service = ResumeBuilderService()
