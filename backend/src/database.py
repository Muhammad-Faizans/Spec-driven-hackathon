from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Make DATABASE_URL optional - use SQLite in-memory if not provided
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    database_available = True
except Exception as e:
    print(f"Database connection failed: {e}")
    print("Running without database support")
    engine = None
    SessionLocal = None
    Base = None
    database_available = False

def get_db():
    if not database_available:
        return None
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
