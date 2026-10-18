from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError
from app.common.response import response


class BusinessException(Exception):
    """业务异常：由全局异常处理器统一转成响应结构"""

    def __init__(self, message: str, code: int = 400):
        self.message = message
        self.code = code
        super().__init__(message)


async def business_exception_handler(request: Request, exc: BusinessException):
    """把业务异常转换成统一响应格式（HTTP 200 + 业务码）"""
    return JSONResponse(
        status_code=200,
        content=response.error(code=exc.code, message=exc.message).model_dump(),
    )

async def http_business_exception_handler(request: Request, exc: HTTPException):
    """Http异常处理器"""
    return JSONResponse(
        status_code=exc.status_code,
        content=response.error(code=exc.status_code, message=exc.detail).model_dump(),
    )

async def vallidation_exception_handler(request: Request, exc: RequestValidationError):
    """参数异常处理器"""
    return JSONResponse(
        status_code=422,
        content=response.error(code=422, message="请求参数错误").model_dump(),
    )

async def global_exception_handler(request: Request, exc: Exception):
    """全局异常处理器"""
    return JSONResponse(
        status_code=422,
        content=response.error(code=422, message="服务器内部错误").model_dump(),
    )
