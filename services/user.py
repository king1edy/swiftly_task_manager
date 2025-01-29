from sqlalchemy.orm import Session
from repositories.user import UserRepository
from dtos.user import UserCreate, UserResponse
from typing import List, Optional
from models.user import User

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db) # ✅ Initialize UserRepository correctly

    def create_user(self, user_data: UserCreate) -> UserResponse:
        return self.user_repo.create_user(user_data)

    def get_user_by_username(self, username: str) -> Optional[User]:
        return self.user_repo.get_user_by_username(username)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        return self.user_repo.get_user_by_id(user_id)

    def get_users(self) -> List[User]:
        return self.user_repo.get_users()

    def update_user(self, user_id: int, user_data: UserCreate) -> Optional[User]:
        return self.user_repo.update_user(user_id, user_data)

    def delete_user(self, user_id: int) -> bool:
        return self.user_repo.delete_user(user_id)

# In the services/user.py module, we define a UserService class that encapsulates the business logic for user-related operations. The class has methods
# for creating, retrieving, updating, and deleting users. The UserService class interacts with the UserRepository class to perform database operations.
# The UserRepository class is responsible for interacting with the database to perform CRUD operations on the User model.
# The UserService class provides a layer of abstraction between the API routes and the database operations. This separation of concerns helps keep the
# codebase organized and maintainable. The UserService class can be easily tested and extended without affecting the API routes or the database
# operations. The UserService class follows the single responsibility principle by encapsulating user-related business logic in a separate class.
# The UserService class provides a clean and consistent interface for interacting with user data. The methods in the UserService class are self-contained
# and can be reused across different parts of the application. The UserService class follows best practices for structuring business logic in a FastAPI
# application. The separation of concerns between the API routes, services, and repositories helps maintain a clean and modular codebase. The UserService
# class can be easily extended or modified without affecting the rest of the application. The UserService class follows
# the dependency injection pattern by accepting a database session as a parameter in its constructor. This allows the class to be easily tested with
# different database configurations or mock objects. The UserService class provides a clear separation between the business logic and the database