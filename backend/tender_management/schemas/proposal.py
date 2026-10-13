from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class ProposalTone(str, Enum):
    FORMAL = "formal"
    CONCISE = "concise"
    TECHNICAL = "technical"
    MARKETING = "marketing"

class CompanyProfile(BaseModel):
    name: str
    expertise: List[str]
    past_projects: List[str]
    achievements: List[str]
    years_of_experience: int
    industry: str

class TenderRequirements(BaseModel):
    title: str
    scope: str
    requirements: List[str]
    budget_range: Optional[str]
    deadline: Optional[str]
    evaluation_criteria: Optional[List[str]]

class ProposalRequest(BaseModel):
    company_profile: CompanyProfile
    tender_requirements: TenderRequirements
    tone: ProposalTone = ProposalTone.FORMAL

class ProposalResponse(BaseModel):
    proposal_text: str
    sections: List[str]
    generated_at: str
    tone: ProposalTone 