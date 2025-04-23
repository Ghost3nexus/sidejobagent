import os
import feedparser
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class JobScraper:
    """Service for scraping job listings from various sources"""
    
    def __init__(self):
        """Initialize the job scraper"""
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
    
    def fetch_rss_feed(self, url: str) -> List[Dict[str, Any]]:
        """Fetch and parse an RSS feed"""
        try:
            feed = feedparser.parse(url)
            return feed.entries
        except Exception as e:
            logger.error(f"Error fetching RSS feed from {url}: {str(e)}")
            return []
    
    def extract_job_details(self, entry: Dict[str, Any], source: str) -> Dict[str, Any]:
        """Extract job details from an RSS entry"""
        job = {
            "title": entry.get("title", ""),
            "description": entry.get("summary", ""),
            "url": entry.get("link", ""),
            "source": self.sources[source]["name"],
            "compensation": "未設定",
            "skills": []
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
    
    def fetch_mock_jobs(self) -> List[Dict[str, Any]]:
        """Fetch mock job data for development"""
        return [
            {
                "title": "フロントエンドエンジニア",
                "description": "React/Next.jsを使用したWebアプリケーション開発",
                "url": "https://example.com/job/1",
                "source": "クラウドワークス",
                "compensation": "6,000円/時",
                "skills": ["React", "Next.js", "TypeScript"]
            },
            {
                "title": "バックエンドエンジニア",
                "description": "Python/FastAPIを使用したAPIサービス開発",
                "url": "https://example.com/job/2",
                "source": "ランサーズ",
                "compensation": "7,000円/時",
                "skills": ["Python", "FastAPI", "PostgreSQL"]
            },
            {
                "title": "UIデザイナー",
                "description": "モバイルアプリのUIデザイン作成",
                "url": "https://example.com/job/3",
                "source": "Anycrew",
                "compensation": "8,000円/時",
                "skills": ["Figma", "UI/UX", "Adobe XD"]
            },
            {
                "title": "Webマーケター",
                "description": "SEO対策とコンテンツマーケティング",
                "url": "https://example.com/job/4",
                "source": "複業クラウド",
                "compensation": "5,000円/時",
                "skills": ["SEO", "コンテンツマーケティング", "Google Analytics"]
            },
            {
                "title": "テクニカルライター",
                "description": "技術ドキュメントの作成",
                "url": "https://example.com/job/5",
                "source": "ITプロパートナーズ",
                "compensation": "4,500円/時",
                "skills": ["技術文書", "Markdown", "API ドキュメント"]
            }
        ]

job_scraper = JobScraper()
