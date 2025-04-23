from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import CORS_ORIGINS, API_PREFIX
from .routers import auth, users, jobs, resume, cover_letter, matching
from .services.crawler import initialize_crawler
import logging

app = FastAPI(title="Side Job Agent API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix=API_PREFIX)
app.include_router(users.router, prefix=API_PREFIX)
app.include_router(jobs.router, prefix=API_PREFIX)
app.include_router(resume.router, prefix=API_PREFIX)
app.include_router(cover_letter.router, prefix=API_PREFIX)
app.include_router(matching.router, prefix=API_PREFIX)

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logging.info("Initializing crawler...")
    initialize_crawler()

@app.get("/")
async def root():
    return {"message": "Welcome to Side Job Agent API"}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}
