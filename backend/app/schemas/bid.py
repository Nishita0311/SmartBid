from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BidBase(BaseModel):
    tender_id: int
    company_id: int
    amount: float
    proposal: str
    documents: Optional[List[str]] = None

class BidCreate(BidBase):
    pass

class BidUpdate(BaseModel):
    amount: Optional[float] = None
    proposal: Optional[str] = None
    documents: Optional[List[str]] = None
    status: Optional[str] = None
    score: Optional[float] = None
    feedback: Optional[str] = None

class BidResponse(BidBase):
    id: int
    user_id: int
    status: str
    score: Optional[float] = None
    feedback: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class BidEvaluation(BaseModel):
    score: float
    feedback: str
    technical_score: float
    financial_score: float
    past_performance_score: float
    domain_expertise_score: float
    evaluation_notes: str 