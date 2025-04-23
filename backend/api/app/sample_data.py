from app.utils.db import db

def create_sample_data():
    """Create sample job data for testing"""
    jobs = [
        {
            'title': 'フロントエンドエンジニア',
            'description': 'React/Next.jsを使用したWebアプリケーション開発',
            'url': 'https://example.com/job/1',
            'source': 'クラウドワークス',
            'compensation': '6,000円/時',
            'skills': ['React', 'Next.js', 'TypeScript']
        },
        {
            'title': 'バックエンドエンジニア',
            'description': 'Python/FastAPIを使用したAPIサービス開発',
            'url': 'https://example.com/job/2',
            'source': 'ランサーズ',
            'compensation': '7,000円/時',
            'skills': ['Python', 'FastAPI', 'PostgreSQL']
        },
        {
            'title': 'UIデザイナー',
            'description': 'モバイルアプリのUIデザイン作成',
            'url': 'https://example.com/job/3',
            'source': 'Anycrew',
            'compensation': '8,000円/時',
            'skills': ['Figma', 'UI/UX', 'Adobe XD']
        }
    ]
    
    for job in jobs:
        db.create_job(job)
    
    print('Sample job data created successfully!')

if __name__ == "__main__":
    create_sample_data()
