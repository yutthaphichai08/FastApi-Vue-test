from sqlalchemy import Boolean, Column, Integer, String
# from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    address = Column(String)
    salary=Column(Integer)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")


