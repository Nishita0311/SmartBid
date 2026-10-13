from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Import routers
from .routers.auth import router as auth_router
from .routers.tenders import router as tenders_router
from .routers.companies import router as companies_router
from .routers.bids import router as bids_router
from .routers.notifications import router as notifications_router
from .routers.analytics import router as analytics_router
from .routers.proposals import router as proposals_router

# Import database
from .database import create_tables

# Load environment variables
load_dotenv()

# Create database tables
create_tables()

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

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["Authentication"])
app.include_router(tenders_router, prefix="/api/tenders", tags=["Tenders"]) 
app.include_router(companies_router, prefix="/api/companies", tags=["Companies"])
app.include_router(bids_router, prefix="/api/bids", tags=["Bids"])
app.include_router(notifications_router, prefix="/api/notifications", tags=["Notifications"])
app.include_router(analytics_router, prefix="/api/analytics", tags=["Analytics"])
app.include_router(proposals_router, prefix="/api/proposals", tags=["Proposals"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Tender Management System API"} 