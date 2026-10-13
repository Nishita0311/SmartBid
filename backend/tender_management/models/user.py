from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_company = Column(Boolean, default=False)

    # Relationships
    company = relationship("Company", back_populates="user", uselist=False)
    bids = relationship("Bid", back_populates="user")
    notifications = relationship("Notification", back_populates="user") 