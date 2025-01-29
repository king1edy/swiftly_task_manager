
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime
from db.base_model import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    date_created = Column(DateTime)
    date_updated = Column(DateTime)
    is_active = Column(Boolean, default=True)

