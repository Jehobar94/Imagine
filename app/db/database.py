from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:22021617@localhost:51924/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocomit=False,autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
        db.close()