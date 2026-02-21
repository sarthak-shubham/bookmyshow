from database import Base
from sqlalchemy import Column, Integer, Text, TIMESTAMP
from sqlalchemy.sql import func

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    duration_minutes = Column(Integer, nullable=False)
    language = Column(Text, nullable=False)
    genre = Column(Text, nullable=False)
    release_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now(), nullable=False)
