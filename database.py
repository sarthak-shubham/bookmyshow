from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

DATABASE_URL = "postgresql://admin:password@localhost:5432/bookmyshow_db"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()