from typing import Optional
from sqlalchemy.orm import Session
from models.user import User
from dtos.user import UserCreate
from core.security import hash_password
from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(User, db)

    def get_by_username(self, username: str) -> Optional[User]:
        """Retrieve a user by username."""
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_username(self, username: str) -> Optional[User]:
        """Retrieve a user by username."""
        return self.get_by_username(username)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Retrieve a user by ID."""
        return self.db.query(User).filter(User.id == user_id).first() # type: ignore

    def get_users(self) -> list[User]:
        """Retrieve all users."""
        return self.db.query(User).all() # type: ignore

    def create_user(self, user_in: UserCreate) -> User:
        """Create a new user and hash their password."""
        user_data = user_in.model_dump()
        user_data["hashed_password"] = hash_password(user_data["password"])
        del user_data["password"]  # Remove plain-text password
        return self.create(user_data)  # Using BaseRepository's create method

    def update_user(self, user_id: int, user_in: UserCreate) -> Optional[User]:
        """Update a user's details."""
        user = self.get(user_id)
        if user:
            user_data = user_in.model_dump()
            user_data["hashed_password"] = hash_password(user_data["password"])
            del user_data["password"]  # Remove plain-text password
            return self.update(user, user_data)  # Using BaseRepository's update method

        return None

    def delete_user(self, user_id: int) -> bool:
        """Delete a user."""
        return self.delete(user_id)  # Using BaseRepository's delete method
# In the repositories/user.py module, we define a UserRepository class that encapsulates database operations related to the User model. The UserRepository
# class inherits from the BaseRepository class, which provides generic CRUD methods for interacting with the database. The UserRepository class provides
# methods for retrieving, creating, updating, and deleting user records. The UserRepository class follows the repository pattern, which separates the
# database operations from the business logic. The UserRepository class provides a clean and consistent interface for interacting with user data. The
# UserRepository class encapsulates the database queries and operations, making it easy to reuse the code across different parts of the application. The
# UserRepository class follows best practices for structuring database operations in a FastAPI application. The separation of concerns between the
# repositories, services, and API routes helps maintain a clean and modular codebase. The UserRepository class provides a layer of abstraction over the
# database operations, making it easy to switch between different database implementations. The UserRepository class follows the single responsibility
# principle by encapsulating user-related database operations in a separate class. The UserRepository class provides methods for common database
# operations such as retrieving users by username or ID, creating new users, updating user details, and deleting users. The UserRepository class
# encapsulates the logic for hashing user passwords when creating or updating user records. The UserRepository class provides a consistent and
# standardized way to interact with the User model in the database. The UserRepository class follows the dependency injection pattern by accepting a
# database session as a parameter in its constructor. This allows the class to be easily tested with different database configurations or mock objects.
# The UserRepository class provides a clean and structured way to interact with the database, improving code readability and maintainability.
