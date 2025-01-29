from sqlalchemy.orm import Session
from repositories.task import TaskRepository
from dtos.task import TaskCreate, TaskUpdate
from typing import List, Optional
from models.task import Task


class TaskService:
    def __init__(self, db: Session):
        self.task_repo = TaskRepository(db)

    def get_tasks_for_user(self, user_id: int) -> List[Task]:
        return self.task_repo.get_user_tasks(user_id)

    def create_task(self, task_data: TaskCreate, user_id: int) -> Task:
        return self.task_repo.create_user_task(task_data, user_id)

    def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
        return self.task_repo.update_task(task_id, task_data)

    def delete_task(self, task_id: int) -> bool:
        return self.task_repo.delete(task_id)
