from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dtos.task import TaskCreate, TaskUpdate, TaskResponse
from services.task import TaskService
from core.security import get_current_user
from db.session import get_db

router = APIRouter()


@router.get("/", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = TaskService(db)
    return service.get_tasks_for_user(current_user)


@router.post("/", response_model=TaskResponse)
def create_task(task_in: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = TaskService(db)
    return service.create_task(task_in, current_user)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db),
                current_user: str = Depends(get_current_user)):
    service = TaskService(db)
    updated_task = service.update_task(task_id, task_in)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    service = TaskService(db)
    if not service.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
