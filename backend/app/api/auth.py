from app.schemas.auth import RegisterRequest
from app.common.exception import BusinessException
from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token
from app.common.response import response
from app.services import auth_service

router = APIRouter(prefix="/auth",tags=["权限验证"])

@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    result = auth_service.login(db,data)
    return response.success(
        message="登录成功",
        data=result
    )

@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    result = auth_service.register(db,data)
    return response.success(
        message="注册成功",
    )
