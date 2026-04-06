from fastapi import Depends,APIRouter,HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.db import models
from app.schemas.user import UserLogin,UserCreate
from app.utils.security import hash_password,verify_password
from app.utils.jwt import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from app.db.models import User
from app.dependencies.auth import get_current_admin

router = APIRouter()

@router.post("/register")
def register(user : UserCreate, db : Session = Depends(get_db)):
    new_user = models.User(email=user.email,password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg" : "user created"}



@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
    "sub": user.email,
    "role": user.role   # 👈 ADD THIS
})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/admin")
def admin_dashboard(admin = Depends(get_current_admin)):
    return {
        "message": "Welcome Admin 🔥",
        "user": admin
    }