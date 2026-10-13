from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
import shutil
import os
from datetime import datetime

from ..database import get_db
from ..models.models import Company, User
from tender_management.schemas.company import CompanyCreate, CompanyResponse, CompanyUpdate

from ..routers.auth import get_current_user

router = APIRouter()

# Configure file upload directory
UPLOAD_DIR = "uploads/company_documents"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", response_model=CompanyResponse)
async def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if user already has a company
    existing_company = db.query(Company).filter(Company.user_id == current_user.id).first()
    if existing_company:
        raise HTTPException(status_code=400, detail="User already has a company profile")
    
    db_company = Company(
        user_id=current_user.id,
        **company.dict()
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/", response_model=List[CompanyResponse])
async def get_companies(
    skip: int = 0,
    limit: int = 100,
    industry: str = None,
    location: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Company)
    
    if industry:
        query = query.filter(Company.industry == industry)
    if location:
        query = query.filter(Company.location == location)
    
    return query.offset(skip).limit(limit).all()

@router.get("/me", response_model=CompanyResponse)
async def get_my_company(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    company = db.query(Company).filter(Company.user_id == current_user.id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company profile not found")
    return company

@router.put("/me", response_model=CompanyResponse)
async def update_company(
    company_update: CompanyUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    company = db.query(Company).filter(Company.user_id == current_user.id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company profile not found")
    
    for field, value in company_update.dict(exclude_unset=True).items():
        setattr(company, field, value)
    
    company.updated_at = datetime.now()
    db.commit()
    db.refresh(company)
    return company

@router.post("/me/documents")
async def upload_company_document(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user)
):
    # Verify file type
    allowed_extensions = {'.pdf', '.doc', '.docx', '.jpg', '.jpeg', '.png'}
    file_extension = os.path.splitext(file.filename)[1].lower()
    if file_extension not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    # Save file
    file_path = os.path.join(UPLOAD_DIR, f"{current_user.id}_{file.filename}")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "path": file_path}

@router.get("/{company_id}", response_model=CompanyResponse)
async def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.get("/search/", response_model=List[CompanyResponse])
async def search_companies(
    query: str,
    db: Session = Depends(get_db)
):
    companies = db.query(Company).filter(
        (Company.name.ilike(f"%{query}%")) |
        (Company.description.ilike(f"%{query}%")) |
        (Company.industry.ilike(f"%{query}%")) |
        (Company.location.ilike(f"%{query}%"))
    ).all()
    return companies

@router.get("/")
async def get_companies():
    return {"message": "List of companies"} 