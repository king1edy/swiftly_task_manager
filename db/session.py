from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# Database Connection
print("Database URL is ", settings.database_url)
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# if you don't want to install postgres or any database, use sqlite, a file system based database,
# uncomment below lines if you would like to use sqlite and comment above 2 lines of SQLALCHEMY_DATABASE_URL AND engine

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# Base Model
Base = declarative_base()


# Dependency Injection for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
