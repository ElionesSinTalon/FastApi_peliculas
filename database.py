from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQL_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, bind=engine)

Base = declarative_base()