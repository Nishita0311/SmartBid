from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Dict
from datetime import datetime, timedelta

from ..database import get_db
from ..models.models import Bid, Tender, Company, User
from ..schemas.analytics import (
    BidSuccessRate,
    CompetitorAnalysis,
    MarketTrends,
    CompanyPerformance
)
from ..routers.auth import get_current_user

router = APIRouter()

@router.get("/")
async def get_analytics():
    return {"message": "Analytics data"}

@router.get("/bid-success-rate/{company_id}", response_model=BidSuccessRate)
async def get_bid_success_rate(
    company_id: int,
    start_date: datetime = None,
    end_date: datetime = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify company exists and belongs to current user
    company = db.query(Company).filter(
        Company.id == company_id,
        Company.user_id == current_user.id
    ).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Set default date range if not provided
    if not start_date:
        start_date = datetime.now() - timedelta(days=365)
    if not end_date:
        end_date = datetime.now()
    
    # Calculate bid success rate
    total_bids = db.query(Bid).filter(
        Bid.company_id == company_id,
        Bid.created_at.between(start_date, end_date)
    ).count()
    
    successful_bids = db.query(Bid).filter(
        Bid.company_id == company_id,
        Bid.status == "accepted",
        Bid.created_at.between(start_date, end_date)
    ).count()
    
    success_rate = (successful_bids / total_bids * 100) if total_bids > 0 else 0
    
    return BidSuccessRate(
        company_id=company_id,
        total_bids=total_bids,
        successful_bids=successful_bids,
        success_rate=success_rate,
        period_start=start_date,
        period_end=end_date
    )

@router.get("/competitor-analysis/{tender_id}", response_model=CompetitorAnalysis)
async def get_competitor_analysis(
    tender_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tender = db.query(Tender).filter(Tender.id == tender_id).first()
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    
    # Get all bids for the tender
    bids = db.query(Bid).filter(Bid.tender_id == tender_id).all()
    
    # Calculate average bid amount
    total_amount = sum(bid.amount for bid in bids)
    avg_amount = total_amount / len(bids) if bids else 0
    
    # Get company details for each bid
    competitors = []
    for bid in bids:
        company = db.query(Company).filter(Company.id == bid.company_id).first()
        if company:
            competitors.append({
                "company_id": company.id,
                "company_name": company.name,
                "bid_amount": bid.amount,
                "past_success_rate": calculate_company_success_rate(db, company.id)
            })
    
    return CompetitorAnalysis(
        tender_id=tender_id,
        total_bids=len(bids),
        average_bid_amount=avg_amount,
        competitors=competitors
    )

@router.get("/market-trends", response_model=MarketTrends)
async def get_market_trends(
    category: str = None,
    location: str = None,
    start_date: datetime = None,
    end_date: datetime = None,
    db: Session = Depends(get_db)
):
    # Set default date range if not provided
    if not start_date:
        start_date = datetime.now() - timedelta(days=365)
    if not end_date:
        end_date = datetime.now()
    
    # Build query
    query = db.query(Tender).filter(
        Tender.created_at.between(start_date, end_date)
    )
    
    if category:
        query = query.filter(Tender.category == category)
    if location:
        query = query.filter(Tender.location == location)
    
    # Get tender statistics
    tenders = query.all()
    total_tenders = len(tenders)
    total_budget = sum(tender.budget for tender in tenders)
    avg_budget = total_budget / total_tenders if total_tenders > 0 else 0
    
    # Get category distribution
    category_distribution = {}
    for tender in tenders:
        category_distribution[tender.category] = category_distribution.get(tender.category, 0) + 1
    
    return MarketTrends(
        total_tenders=total_tenders,
        total_budget=total_budget,
        average_budget=avg_budget,
        category_distribution=category_distribution,
        period_start=start_date,
        period_end=end_date
    )

@router.get("/company-performance/{company_id}", response_model=CompanyPerformance)
async def get_company_performance(
    company_id: int,
    start_date: datetime = None,
    end_date: datetime = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify company exists and belongs to current user
    company = db.query(Company).filter(
        Company.id == company_id,
        Company.user_id == current_user.id
    ).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Set default date range if not provided
    if not start_date:
        start_date = datetime.now() - timedelta(days=365)
    if not end_date:
        end_date = datetime.now()
    
    # Get all bids for the company in the specified period
    bids = db.query(Bid).filter(
        Bid.company_id == company_id,
        Bid.created_at.between(start_date, end_date)
    ).all()
    
    # Calculate performance metrics
    total_bids = len(bids)
    successful_bids = sum(1 for bid in bids if bid.status == "accepted")
    success_rate = (successful_bids / total_bids * 100) if total_bids > 0 else 0
    
    # Get average bid amount
    total_amount = sum(bid.amount for bid in bids)
    avg_amount = total_amount / total_bids if total_bids > 0 else 0
    
    # Get category distribution
    category_distribution = {}
    for bid in bids:
        tender = db.query(Tender).filter(Tender.id == bid.tender_id).first()
        if tender:
            category_distribution[tender.category] = category_distribution.get(tender.category, 0) + 1
    
    return CompanyPerformance(
        company_id=company_id,
        total_bids=total_bids,
        successful_bids=successful_bids,
        success_rate=success_rate,
        average_bid_amount=avg_amount,
        category_distribution=category_distribution,
        period_start=start_date,
        period_end=end_date
    )

def calculate_company_success_rate(db: Session, company_id: int) -> float:
    total_bids = db.query(Bid).filter(Bid.company_id == company_id).count()
    successful_bids = db.query(Bid).filter(
        Bid.company_id == company_id,
        Bid.status == "accepted"
    ).count()
    return (successful_bids / total_bids * 100) if total_bids > 0 else 0 