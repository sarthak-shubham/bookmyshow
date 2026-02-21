from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey

class Screen(Base):
    __tablename__ = "screens"

    id = Column(Integer, primary_key=True, index=True)
    theatre_id = Column(Integer, ForeignKey("theatres.id"), nullable=False)
    name = Column(Text, nullable=False)
    total_seats = Column(Integer, nullable=False)
