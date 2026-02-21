from database import Base
from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func

class Theatre(Base):
    __tablename__ = "theatres"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    city = Column(Text, nullable=False)
    address = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
