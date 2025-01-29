# main.py
from fastapi import FastAPI, Depends
from core.config import settings

from core.config import Settings
from core.security import get_current_user
from db.session import engine
from db.base_model import Base

# from routes.user import router as user_router
from routes.tasks import router as task_router


# Create all tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)


# Create and configure the FastAPI application
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    create_tables()  # Ensure tables are created at startup
    # app.include_router(user_router, prefix="/api/users", tags=["Users"])
    app.include_router(task_router, prefix="/api/tasks", tags=["Tasks"])
    return app


# Instantiate the app
app = start_application()


@app.get("/")
def hello_api():
    return {"msg": "Hello FastAPI🚀"}


@app.get("/protected-route")
def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Welcome, {current_user}!"}

