from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_user
from app.model.user import User
from app.schemas.user import UserResponse
from app.common.response import response

router = APIRouter(prefix="/user", tags=["用户管理"])

@router.get("/info")
def get_user_info(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息
    """
    return response.success(message="获取用户信息成功", data=UserResponse.model_validate(current_user))