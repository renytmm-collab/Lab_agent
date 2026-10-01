from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserResponse

router = APIRouter(prefix="/api/auth",tags=["权限验证"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user=db.query(User).filter(User.username == data.username).first()
    
    #判断账号密码是否正确
    if not user or user.password != data.password:
        return {"code":400,"message":"账号或者密码错误"}
    return {
        "code":200,
        "message":"登录成功",
        "data": UserResponse.model_validate(user),
        }

