from fastapi import FastAPI
from app.routers import papers

app = FastAPI(title="Research Editor API")

# Include routers
app.include_router(papers.router, prefix="/papers", tags=["papers"])
