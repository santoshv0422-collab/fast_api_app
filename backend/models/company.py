from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    location = Column(String)
    jobs = relationship("Job", back_populates="company", lazy="selectin")

# Ensure the Job model is imported so SQLAlchemy can resolve the Company.jobs relationship
from . import job
    