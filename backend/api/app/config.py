import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")

SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-for-development")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

CORS_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://sidejobagent.vercel.app",
    "*"  # For development
]

API_PREFIX = "/api"
