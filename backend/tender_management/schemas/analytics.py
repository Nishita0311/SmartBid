from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime

class BidSuccessRate(BaseModel):
    company_id: int
    total_bids: int
    successful_bids: int
    success_rate: float
    period_start: datetime
    period_end: datetime

class CompetitorInfo(BaseModel):
    company_id: int
    company_name: str
    bid_amount: float
    past_success_rate: float

class CompetitorAnalysis(BaseModel):
    tender_id: int
    total_bids: int
    average_bid_amount: float
    competitors: List[CompetitorInfo]

class MarketTrends(BaseModel):
    total_tenders: int
    total_budget: float
    average_budget: float
    category_distribution: Dict[str, int]
    period_start: datetime
    period_end: datetime

class CompanyPerformance(BaseModel):
    company_id: int
    total_bids: int
    successful_bids: int
    success_rate: float
    average_bid_amount: float
    category_distribution: Dict[str, int]
    period_start: datetime
    period_end: datetime 