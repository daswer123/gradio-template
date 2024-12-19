from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Settings(Base):
    __tablename__ = 'settings'
    
    id = Column(Integer, primary_key=True)
    volume = Column(Float, default=1.0)
    sample_rate = Column(Integer, default=44100)
    output_format = Column(String, default='wav')