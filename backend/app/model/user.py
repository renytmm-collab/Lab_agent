from app.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"comment": "用户信息表"}
    username:Mapped[str]=mapped_column(String(50), comment="账号",nullable=False)
    password:Mapped[str]=mapped_column(String(50), comment="密码",nullable=False)
    role:Mapped[str]=mapped_column(String(50), comment="角色：student-学生，admin-管理员",nullable=False)
    name:Mapped[str]=mapped_column(String(50), comment="",nullable=False)
    email:Mapped[str|None]=mapped_column(String(50), comment="邮箱")
    phone:Mapped[str|None]=mapped_column(String(50), comment="手机号")
    avatar:Mapped[str|None]=mapped_column(String(50), comment="头像")
    status:Mapped[int]=mapped_column(default=1, comment="状态：0-禁用，1-正常")