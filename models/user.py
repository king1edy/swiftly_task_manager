from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.base_model import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    date_created = Column(DateTime(timezone=True), server_default=func.now())
    date_updated = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner", cascade="all, delete")


