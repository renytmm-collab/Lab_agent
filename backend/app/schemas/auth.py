from app.schemas.user import UserResponse
from pydantic import BaseModel, Field, field_validator

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    token: str
    user: UserResponse

class RegisterRequest(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    password: str = Field(min_length=1)
    name: str | None = Field(default=None, max_length=50)

    @field_validator('username')
    @classmethod
    def validate_username(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('账号不能为空')
        return value

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if len(value.encode('utf-8')) > 72:
            raise ValueError('密码不能超过72字节')
        return value
