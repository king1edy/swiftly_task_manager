from typing import Type, TypeVar, Generic, List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from db.base_model import Base  # Importing the SQLAlchemy Base model

# Define generic types for SQLAlchemy models
ModelType = TypeVar("ModelType", bound=Base)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db: Session):
        """
        Generic repository for CRUD operations.
        :param model: SQLAlchemy model class
        :param db: SQLAlchemy session
        """
        self.model = model
        self.db = db

    def get(self, id: int) -> Optional[ModelType]:
        """
        Fetch a single record by primary key.
        """
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self) -> List[ModelType]:
        """
        Fetch all records from the database.
        """
        return self.db.query(self.model).all()

    def create(self, obj_in: dict) -> ModelType:
        """
        Create a new record in the database.
        :param obj_in: Dictionary containing data to create the record.
        """
        try:
            new_record = self.model(**obj_in)
            self.db.add(new_record)
            self.db.commit()
            self.db.refresh(new_record)
            return new_record
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error creating {self.model.__name__}: {str(e)}")

    def update(self, id: int, obj_in: dict) -> Optional[ModelType]:
        """
        Update an existing record.
        :param id: Primary key of the record to update.
        :param obj_in: Dictionary containing updated fields.
        """
        record = self.get(id)
        if not record:
            return None  # Record not found

        try:
            for field, value in obj_in.items():
                setattr(record, field, value)
            self.db.commit()
            self.db.refresh(record)
            return record
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error updating {self.model.__name__}: {str(e)}")

    def delete(self, id: int) -> bool:
        """
        Delete a record by ID.
        :param id: Primary key of the record to delete.
        :return: True if deletion was successful, False otherwise.
        """
        record = self.get(id)
        if not record:
            return False

        try:
            self.db.delete(record)
            self.db.commit()
            return True
        except SQLAlchemyError as e:
            self.db.rollback()
            raise Exception(f"Error deleting {self.model.__name__}: {str(e)}")
