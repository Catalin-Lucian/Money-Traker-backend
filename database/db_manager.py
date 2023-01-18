from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./records.sqlite"

# Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Create the base class
Base = declarative_base()


def create_db():
    Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    emailConfirmed = Column(Boolean, default=False)
    password = Column(String)


class Deposit(Base):
    __tablename__ = "deposits"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, default="Deposit")
    amount = Column(Float, default=0)
    ico_name = Column(String, default="coin")


class Operation(Base):
    __tablename__ = "operations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    deposit_id = Column(Integer, ForeignKey("deposits.id"))
    amount = Column(Float)
    date = Column(DateTime, default=datetime.now())
    optype = Column(String, default="unknown")
