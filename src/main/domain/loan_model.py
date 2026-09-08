from pydantic import BaseModel, Field, validator
from sqlalchemy import Column, Integer, Float, Date, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()


class LoanCreate(BaseModel):
    amount: float = Field(..., gt=0)
    interest_rate: float = Field(..., gt=0)
    due_date: date = Field(..., gt=date.today())
    status: str = Field(..., regex='^(active|inactive)$')


class LoanUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    interest_rate: Optional[float] = Field(None, gt=0)
    due_date: Optional[date] = Field(None, gt=date.today())
    status: Optional[str] = Field(None, regex='^(active|inactive)$')


class Loan(Base):
    __tablename__ = 'loans'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)