from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship

from database import Base


class Application(Base):
    __tablename__ = "application"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    address = Column(String)
    salary=Column(Integer)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")
    
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)





