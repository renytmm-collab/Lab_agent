from fastapi import APIRouter,Depends
from app.schemas.auth import LoginRequest
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.user import User
from app.schemas.user import UserResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/user",tags=["权限验证"])

@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息
    """
    return {
        "code": 200,
        "message": "获取成功",
        "data": UserResponse.model_validate(current_user)
    }