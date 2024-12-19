from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Settings(Base):
    __tablename__ = 'settings'
    
    id = Column(Integer, primary_key=True)
    component = Column(String, nullable=False)
    key = Column(String, nullable=False)
    value = Column(String, nullable=False)