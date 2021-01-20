from datetime import datetime
from sqlalchemy import (Column, Integer, String, DateTime)
from sqlalchemy.types import Date
from .database import Base

class User(Base):
    __tablename__ = "Users"

    id = Column('user_id', Integer(), primary_key=True)
    username = Column('username', String(15), nullable=False, unique=True)
    email = Column('email_address', String(255), nullable=False)
    phoneNumber = Column('phone', String(20), nullable=False)
    password = Column('password', String(25), nullable=False)
    created_on = Column('created_on', DateTime(), default=datetime.now)
    updated_on = Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
    