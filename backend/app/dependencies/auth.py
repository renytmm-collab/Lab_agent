from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.utils.jwt import decode_access_token
from app.model.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db))->User:
    """
    获取当前用户信息
    """
    #decode_access_token 遇到过期/非法 token 时返回 None，不会抛异常，所以要判 None
    payload=decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token无效或已过期")
    #从数据库根据用户查询用户信息
    user_id=payload.get("user_id")
    if not user_id:
        raise HTTPException(status_code=401, detail="Token无效")
    user=db.query(User).filter(User.id==user_id).first()
    #token 签名合法但用户可能已被删除
    if not user:
        raise HTTPException(status_code=401, detail="用户不存在")
    if user.status!=1:
        raise HTTPException(status_code=403, detail="账号已被禁用")
    return user
