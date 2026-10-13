from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    address: str

class CompanyResponse(BaseModel):
    id: int
    name: str
    address: str

class CompanyUpdate(BaseModel):
    name: str = None
    address: str = None
