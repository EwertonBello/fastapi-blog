from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80))
    email = Column(String(100))
    password = Column(String(200))

    blogs = relationship('Blog', back_populates="creator")
