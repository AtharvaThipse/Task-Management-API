from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.db import models
from app.core.redis_client import redis_client
import json

router = APIRouter()

@router.post("/tasks")
def create_taks(title : str,description : str ,db : Session = Depends(get_db)):
    task = models.Task(title=title,description=description)
    db.add(task)
    db.commit()
    redis_client.delete("tasks")
    return {"msg" : "task created"}

# @router.get("/tasks")
# def get_tasks(skip : int=0,limit : int =10,db: Session = Depends(get_db)):
#     return db.query(models.Task).offset(skip).limit(limit).all()
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    # 1. Check cache
    cached_tasks = redis_client.get("tasks")

    if cached_tasks:
        return {
            "source": "cache",
            "data": json.loads(cached_tasks)
        }

    # 2. Fetch from DB
    tasks = db.query(models.Task).all()

    # Convert to serializable format
    task_list = [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status
        }
        for t in tasks
    ]

    # 3. Store in Redis (expire in 60 sec)
    redis_client.set("tasks", json.dumps(task_list), ex=60)

    return {
        "source": "db",
        "data": task_list
    }



@router.put("/tasks/{task_id}")
def update_task(task_id : int, status : str,db : Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    task.status = status
    db.commit()
    redis_client.delete("tasks")
    return {"msg" : "Updated"}

@router.delete("/tasks/{task_id}")
def delete_task(task_id : int,db : Session = Depends(get_db)):
    task  = db.query(models.Task).filter(models.Task.id == task_id).first()
    db.delete(task)
    db.commit()
    redis_client.delete("tasks")
    return {"msg" : "Deleted"}