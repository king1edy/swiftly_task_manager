from fastapi import APIRouter, Depends, HTTPException
from dtos.user import UserCreate, UserResponse
from services.user import UserService
from sqlalchemy.orm import Session

from core.security import verify_password, create_access_token
from db.session import get_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)  # ✅ Create an instance of UserService
    existing_user = user_service.get_user_by_username(username=user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists.")
    return user_service.create_user(user)


@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user_service = UserService(db)  # ✅ Create an instance of UserService
    user = user_service.get_user_by_username(username=username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials.")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}