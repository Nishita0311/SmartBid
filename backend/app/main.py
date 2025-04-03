from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Tender Management System",
    description="A comprehensive platform for managing tenders and streamlining the bidding process",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routers
from app.routers import (
    auth,
    tenders,
    companies,
    bids,
    notifications,
    analytics
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(tenders.router, prefix="/api/tenders", tags=["Tenders"])
app.include_router(companies.router, prefix="/api/companies", tags=["Companies"])
app.include_router(bids.router, prefix="/api/bids", tags=["Bids"])
app.include_router(notifications.router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Tender Management System API"} 