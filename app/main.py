from fastapi import FastAPI,Depends
from app.db.database import Base,engine
from app.db import models
from app.api.routes import auth,tasks
from app.dependencies.auth import get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "Task Management API")

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def home():
    return {"Message" : " Api Is Running "}

@app.get("/me")
def get_me(current_user = Depends(get_current_user)):
    return current_user

