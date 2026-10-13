from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from ..database import get_db
from ..models.models import Bid, Tender, Company, User
from ..schemas.bid import BidCreate, BidResponse, BidUpdate
from ..routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=BidResponse)
async def create_bid(
    bid: BidCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Verify tender exists and is open
    tender = db.query(Tender).filter(Tender.id == bid.tender_id).first()
    if not tender:
        raise HTTPException(status_code=404, detail="Tender not found")
    if tender.status != "open":
        raise HTTPException(status_code=400, detail="Tender is not open for bidding")
    
    # Verify company exists
    company = db.query(Company).filter(Company.id == bid.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    # Verify company belongs to current user
    if company.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to bid for this company")
    
    # Create bid
    db_bid = Bid(
        tender_id=bid.tender_id,
        company_id=bid.company_id,
        user_id=current_user.id,
        amount=bid.amount,
        proposal=bid.proposal,
        documents=bid.documents,
        status="submitted"
    )
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid

@router.get("/", response_model=List[BidResponse])
async def get_bids(
    tender_id: int = None,
    company_id: int = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Bid)
    
    if tender_id:
        query = query.filter(Bid.tender_id == tender_id)
    if company_id:
        query = query.filter(Bid.company_id == company_id)
    
    return query.all()

@router.get("/{bid_id}", response_model=BidResponse)
async def get_bid(
    bid_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    bid = db.query(Bid).filter(Bid.id == bid_id).first()
    if not bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    
    # Verify user has access to this bid
    if bid.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this bid")
    
    return bid

@router.put("/{bid_id}", response_model=BidResponse)
async def update_bid(
    bid_id: int,
    bid_update: BidUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_bid = db.query(Bid).filter(Bid.id == bid_id).first()
    if not db_bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    
    # Verify user has access to this bid
    if db_bid.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this bid")
    
    # Verify bid is still editable
    if db_bid.status != "submitted":
        raise HTTPException(status_code=400, detail="Bid cannot be updated in current status")
    
    for field, value in bid_update.dict(exclude_unset=True).items():
        setattr(db_bid, field, value)
    
    db.commit()
    db.refresh(db_bid)
    return db_bid

@router.delete("/{bid_id}")
async def delete_bid(
    bid_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_bid = db.query(Bid).filter(Bid.id == bid_id).first()
    if not db_bid:
        raise HTTPException(status_code=404, detail="Bid not found")
    
    # Verify user has access to this bid
    if db_bid.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this bid")
    
    # Verify bid is still editable
    if db_bid.status != "submitted":
        raise HTTPException(status_code=400, detail="Bid cannot be deleted in current status")
    
    db.delete(db_bid)
    db.commit()
    return {"message": "Bid deleted successfully"}

@router.get("/")
async def get_bids():
    return {"message": "List of bids"} 