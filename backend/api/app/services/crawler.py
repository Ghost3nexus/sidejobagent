import os
import feedparser
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from datetime import datetime
import logging
import time
from apscheduler.schedulers.background import BackgroundScheduler

from ..utils.db import db

logger = logging.getLogger(__name__)

class JobCrawler:
    """Service for crawling job listings from various sources"""
    
    def __init__(self):
        """Initialize the job crawler"""
        self.sources = {
            "crowdworks": {
                "name": "クラウドワークス",
                "rss_url": "https://crowdworks.jp/public/jobs/search.rss?category_id=226&keep_search_criteria=true",
                "base_url": "https://crowdworks.jp"
            },
            "lancers": {
                "name": "ランサーズ",
                "rss_url": "https://www.lancers.jp/work/search/system?open=true&type%5B%5D=project&sort=started&format=rss",
                "base_url": "https://www.lancers.jp"
            }
        }
        
        self.scheduler = BackgroundScheduler()
        self.scheduler.add_job(self.run_scheduled_crawl, 'interval', hours=6)
        self.scheduler.start()
        
    def fetch_rss_feed(self, url: str) -> List[Dict[str, Any]]:
        """Fetch and parse an RSS feed"""
        try:
            feed = feedparser.parse(url)
            return feed.entries
        except Exception as e:
            logger.error(f"Error fetching RSS feed from {url}: {str(e)}")
            return []
    
    def extract_skills_from_description(self, description: str) -> List[str]:
        """Extract skills from job description"""
        common_skills = [
            "Python", "JavaScript", "TypeScript", "React", "Next.js", "Vue.js", "Angular",
            "Node.js", "Django", "Flask", "FastAPI", "Ruby", "Rails", "PHP", "Laravel",
            "Java", "Spring", "C#", ".NET", "Go", "Rust", "Swift", "Kotlin",
            "HTML", "CSS", "SCSS", "SQL", "PostgreSQL", "MySQL", "MongoDB", "Redis",
            "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Git",
            "UI/UX", "Figma", "Adobe XD", "Photoshop", "Illustrator",
            "SEO", "SEM", "Google Analytics", "Marketing", "Content Writing"
        ]
        
        found_skills = []
        for skill in common_skills:
            if skill.lower() in description.lower():
                found_skills.append(skill)
        
        return found_skills
    
    def extract_compensation_from_description(self, description: str) -> str:
        """Extract compensation information from job description"""
        compensation = "未設定"
        
        patterns = [
            r"(\d{1,3}(,\d{3})*円)",  # 10,000円
            r"(時給\s*\d{1,3}(,\d{3})*円)",  # 時給 1,000円
            r"(月額\s*\d{1,3}(,\d{3})*円)",  # 月額 100,000円
            r"(\d{1,3}(,\d{3})*円/時間)",  # 1,000円/時間
            r"(\d{1,3}(,\d{3})*円/月)",  # 100,000円/月
        ]
        
        for pattern in patterns:
            import re
            match = re.search(pattern, description)
            if match:
                compensation = match.group(1)
                break
        
        return compensation
    
    def extract_job_details(self, entry: Dict[str, Any], source: str) -> Dict[str, Any]:
        """Extract job details from an RSS entry"""
        description = entry.get("summary", "")
        
        job = {
            "title": entry.get("title", ""),
            "description": description,
            "url": entry.get("link", ""),
            "source": self.sources[source]["name"],
            "compensation": self.extract_compensation_from_description(description),
            "skills": self.extract_skills_from_description(description)
        }
        
        return job
    
    def fetch_jobs_from_source(self, source: str, limit: int = 10) -> List[Dict[str, Any]]:
        """Fetch jobs from a specific source"""
        if source not in self.sources:
            logger.error(f"Unknown source: {source}")
            return []
        
        source_config = self.sources[source]
        entries = self.fetch_rss_feed(source_config["rss_url"])
        
        jobs = []
        for entry in entries[:limit]:
            job = self.extract_job_details(entry, source)
            jobs.append(job)
        
        return jobs
    
    def fetch_all_jobs(self, limit_per_source: int = 10) -> List[Dict[str, Any]]:
        """Fetch jobs from all sources"""
        all_jobs = []
        
        for source in self.sources:
            jobs = self.fetch_jobs_from_source(source, limit_per_source)
            all_jobs.extend(jobs)
        
        return all_jobs
    
    def save_jobs_to_db(self, jobs: List[Dict[str, Any]]) -> None:
        """Save jobs to database"""
        for job in jobs:
            existing_job = db.get_job_by_url(job["url"])
            if not existing_job:
                db.create_job(job)
    
    def run_scheduled_crawl(self) -> None:
        """Run scheduled crawl job"""
        logger.info("Running scheduled job crawl...")
        jobs = self.fetch_all_jobs()
        self.save_jobs_to_db(jobs)
        logger.info(f"Crawled and saved {len(jobs)} jobs")
    
    def run_initial_crawl(self) -> None:
        """Run initial crawl job"""
        logger.info("Running initial job crawl...")
        jobs = self.fetch_all_jobs()
        self.save_jobs_to_db(jobs)
        logger.info(f"Crawled and saved {len(jobs)} jobs")

job_crawler = JobCrawler()

def initialize_crawler():
    """Initialize crawler with initial data"""
    job_crawler.run_initial_crawl()
