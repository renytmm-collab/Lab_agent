from app.config import settings
from datetime import datetime,timedelta
import jwt

def create_access_token(user_id:int):
    """创建JWTtoken"""
    expire=datetime.now()+timedelta(hours=settings.JWT_EXPIRE_HOURS)
    payload={
        "user_id":user_id,
        "exp": expire
    }
    token=jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)
    return token

def decode_access_token(token:str)->dict|None:
    """解码JWTtoken"""
    try:
        payload=jwt.decode(token,settings.JWT_SECRET_KEY,algorithms=[settings.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


