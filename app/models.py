from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base




class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    requester = relationship("Requester", back_populates="owner")
    days = relationship("Week", back_populates="user")


class Requester(Base):
    __tablename__ = "requester"

    id = Column(Integer, primary_key=True, index=True)
    dow = Column(Integer)
    attendance = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="requester")


#criar week, linkar com user, user_id, dia da semana

class Week(Base):
    __tablename__="days"

    id = Column(Integer, primary_key=True, index = True)
    days = Column(Date)
    user = relationship("Users", back_populates="days")
    user_id = Column(Integer, ForeignKey("users.id"))

class Kitchen(Base):
    __tablename__ = "kitchen"

    id = Column(Integer, primary_key = True, index = True)
    menu = Column(String)

    