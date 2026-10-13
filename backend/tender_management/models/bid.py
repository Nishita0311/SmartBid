from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, Text, String
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    proposal = Column(Text)
    status = Column(String)  # pending, accepted, rejected
    created_at = Column(DateTime, default=datetime.utcnow)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))

    # Relationships
    tender = relationship("Tender", back_populates="bids")
    user = relationship("User", back_populates="bids")
    company = relationship("Company", back_populates="bids") 