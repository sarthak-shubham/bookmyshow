from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey

class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    screen_id = Column(Integer, ForeignKey("screens.id"), nullable=False)
    seat_number = Column(Integer, nullable=False)
    row_label = Column(Text, nullable=False)
    seat_type = Column(Text, nullable=False)
