from app.utils.password import hash_password
from app.schemas.auth import RegisterRequest, LoginRequest, LoginResponse
from sqlalchemy.orm import Session
from app.schemas.auth import LoginRequest
from app.model.user import User
from app.schemas.user import UserResponse
from app.schemas.auth import LoginResponse
from app.utils.password import verify_password
from app.utils.jwt import create_access_token
from app.database import get_db
from app.common.exception import BusinessException

def login(db:Session,data:LoginRequest):
    user=db.query(User).filter(User.username == data.username).first()
    
    #判断账号密码是否正确
    if not user or not verify_password(data.password, user.password):
        raise BusinessException(code=400, message="账号或密码错误")
    #验证账号状态
    if user.status!=1:
        raise BusinessException(code=403, message="账号已经被禁用")
    #生成token
    access_token = create_access_token(user.id)  
    return LoginResponse(token=access_token,user=UserResponse.model_validate(user))

def register(db:Session,data:RegisterRequest):
    user=db.query(User).filter(User.username == data.username).first()
    if user:
        raise BusinessException(code=400, message="用户名已存在")
    new_user=User(
        username=data.username,
        password=hash_password(data.password),
        name=data.name or data.username,
        role="student",
        status=1
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
