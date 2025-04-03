from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from ..database import get_db
from ..models.models import Tender, User
from ..schemas.tender import TenderCreate, TenderResponse, TenderUpdate
from ..routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=TenderResponse)
async def create_tender(
    tender: TenderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_tender = Tender(
        title=tender.title,
        description=tender.description,
        category=tender.category,
        requirements=tender.requirements,
        budget=tender.budget,
        deadline=tender.deadline,
        status="open",
        location=tender.location,
        issuer=tender.issuer,
        contact_info=tender.contact_info,
        documents=tender.documents
    )
    db.add(db_tender)
    db.commit()
    db.refresh(db_tender)
    return db_tender

@router.get("/", response_model=List[TenderResponse])
async def get_tenders(
    skip: int = 0,
    limit: int = 100,
    category: Optional[str] = None,
    status: Optional[str] = None,
    location: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Tender)
    
    if category:
        query = query.filter(Tender.category == category)
    if status:
        query = query.filter(Tender.status == status)
    if location:
        query = query.filter(Tender.location == location)
    
    return query.offset(skip).limit(limit).all()

@router.get("/{tender_id}", response_model=TenderResponse)
async def get_tender(tender_id: int, db: Session = Depends(get_db)):
    tender = db.query(Tender).filter(Tender.id == tender_id).first()
    if tender is None:
        raise HTTPException(status_code=404, detail="Tender not found")
    return tender

@router.put("/{tender_id}", response_model=TenderResponse)
async def update_tender(
    tender_id: int,
    tender_update: TenderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_tender = db.query(Tender).filter(Tender.id == tender_id).first()
    if db_tender is None:
        raise HTTPException(status_code=404, detail="Tender not found")
    
    for field, value in tender_update.dict(exclude_unset=True).items():
        setattr(db_tender, field, value)
    
    db.commit()
    db.refresh(db_tender)
    return db_tender

@router.delete("/{tender_id}")
async def delete_tender(
    tender_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_tender = db.query(Tender).filter(Tender.id == tender_id).first()
    if db_tender is None:
        raise HTTPException(status_code=404, detail="Tender not found")
    
    db.delete(db_tender)
    db.commit()
    return {"message": "Tender deleted successfully"}

@router.get("/search/", response_model=List[TenderResponse])
async def search_tenders(
    query: str = Query(..., description="Search query for tenders"),
    db: Session = Depends(get_db)
):
    # Basic search implementation - can be enhanced with full-text search
    tenders = db.query(Tender).filter(
        (Tender.title.ilike(f"%{query}%")) |
        (Tender.description.ilike(f"%{query}%")) |
        (Tender.category.ilike(f"%{query}%"))
    ).all()
    return tenders 