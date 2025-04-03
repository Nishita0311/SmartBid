from pydantic import BaseModel
from typing import List, Optional, Dict
from datetime import datetime

class TenderBase(BaseModel):
    title: str
    description: str
    category: str
    requirements: List[str]
    budget: float
    deadline: datetime
    location: str
    issuer: str
    contact_info: Dict[str, str]
    documents: Optional[List[str]] = None

class TenderCreate(TenderBase):
    pass

class TenderUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    requirements: Optional[List[str]] = None
    budget: Optional[float] = None
    deadline: Optional[datetime] = None
    status: Optional[str] = None
    location: Optional[str] = None
    issuer: Optional[str] = None
    contact_info: Optional[Dict[str, str]] = None
    documents: Optional[List[str]] = None

class TenderResponse(TenderBase):
    id: int
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class TenderSearchResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    budget: float
    deadline: datetime
    status: str
    location: str
    issuer: str

    class Config:
        orm_mode = True 