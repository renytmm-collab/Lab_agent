from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

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


async def http_business_exception_handler(request: Request, exc: StarletteHTTPException):
    """HTTPException（含 404/405/401）也转成统一结构，保留真实状态码"""
    return JSONResponse(
        status_code=exc.status_code,
        content=response.error(code=exc.status_code, message=str(exc.detail)).model_dump(),
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """参数校验失败：把具体字段和原因带出来"""
    first = exc.errors()[0]
    loc = ".".join(str(x) for x in first.get("loc", []))
    msg = f"{loc}: {first.get('msg', '请求参数错误')}"
    return JSONResponse(
        status_code=422,
        content=response.error(code=422, message=msg).model_dump(),
    )


async def global_exception_handler(request: Request, exc: Exception):
    """全局兜底：未捕获异常统一返回 500"""
    return JSONResponse(
        status_code=500,
        content=response.error(code=500, message="服务器内部错误").model_dump(),
    )
