from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token

router = APIRouter(prefix="/auth",tags=["权限验证"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    user=db.query(User).filter(User.username == data.username).first()
    
    #判断账号密码是否正确
    if not user or not verify_password(data.password, user.password):
        return {"code":400,"message":"账号或者密码错误"}
    #验证账号状态
    if user.status!=1:
        return {"code":403,"message":"账号已被禁用"}
    #生成token
    access_token = create_access_token(user.id)
    return {
        "code":200,
        "message":"登录成功",
        "data": {
            "access_token": access_token,
            "user":UserResponse.model_validate(user)
        }
    }

