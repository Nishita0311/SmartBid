from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_company = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    company = relationship("Company", back_populates="user", uselist=False)
    bids = relationship("Bid", back_populates="user")

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(Text)
    industry = Column(String)
    specialization = Column(JSON)  # List of specializations
    location = Column(String)
    website = Column(String)
    established_year = Column(Integer)
    employee_count = Column(Integer)
    certifications = Column(JSON)  # List of certifications
    past_projects = Column(JSON)  # List of past projects
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="company")
    bids = relationship("Bid", back_populates="company")

class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    category = Column(String)
    requirements = Column(JSON)  # List of requirements
    budget = Column(Float)
    deadline = Column(DateTime(timezone=True))
    status = Column(String)  # open, closed, awarded
    location = Column(String)
    issuer = Column(String)
    contact_info = Column(JSON)
    documents = Column(JSON)  # List of document URLs
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    bids = relationship("Bid", back_populates="tender")

class Bid(Base):
    __tablename__ = "bids"

    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Float)
    proposal = Column(Text)
    documents = Column(JSON)  # List of document URLs
    status = Column(String)  # submitted, under_review, accepted, rejected
    score = Column(Float, nullable=True)
    feedback = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    tender = relationship("Tender", back_populates="bids")
    company = relationship("Company", back_populates="bids")
    user = relationship("User", back_populates="bids")

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    message = Column(Text)
    type = Column(String)  # alert, reminder, update
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 