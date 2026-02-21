from database import Base
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, Numeric, Text
from sqlalchemy.sql import func

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    show_id = Column(Integer, ForeignKey("shows.id"), nullable=False)
    total_price = Column(Numeric, nullable=False)
    status = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
