from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    is_company: bool = False

class UserCreate(UserBase):
    password: str
    company_name: Optional[str] = None
    company_description: Optional[str] = None
    industry: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    name: str
    description: str
    industry: str
    specialization: List[str]
    location: str
    website: Optional[str] = None
    established_year: Optional[int] = None
    employee_count: Optional[int] = None
    certifications: Optional[List[str]] = None
    past_projects: Optional[List[str]] = None

class CompanyCreate(CompanyBase):
    pass

class CompanyResponse(CompanyBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True 