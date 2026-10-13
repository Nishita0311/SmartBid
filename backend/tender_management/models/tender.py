from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    budget = Column(Float)
    deadline = Column(DateTime)
    requirements = Column(Text)
    status = Column(String)  # draft, published, closed, awarded
    created_at = Column(DateTime, default=datetime.utcnow)
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relationships
    company = relationship("Company", back_populates="tenders")
    bids = relationship("Bid", back_populates="tender") 