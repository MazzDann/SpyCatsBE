from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv as Load
Load()

engine = create_engine(os.getenv("db_url"), connect_args={"check_same_thread": False})
SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()