from typing import Optional
from sqlalchemy.orm import Session
from models.user import User
from dtos.user import UserCreate
from core.security import hash_password
from base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_username(self, username: str) -> Optional[User]:
        """Retrieve a user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def create_user(self, user_in: UserCreate) -> User:
        """Create a new user and hash their password."""
        user_data = user_in.model_dump()
        user_data["hashed_password"] = hash_password(user_data["password"])
        del user_data["password"]  # Remove plain-text password
        return self.create(user_data)  # Using BaseRepository's create method
