from pydantic import BaseModel
from typing import Any

class response(BaseModel):
    """统一封装的返回格式"""
    code:int
    message:str
    data: Any=None

    @classmethod
    def success(cls,message:str="请求成功",data:Any=None):
        return cls(code=200,message=message,data=data)
    
    @classmethod
    def error(cls,code:int=500,message:str="请求失败"):
        return cls(code=code,message=message)
    
