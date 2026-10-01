from sqlalchemy.orm import sessionmaker,DeclarativeBase,Mapped,mapped_column
from sqlalchemy import create_engine,DateTime
from app.config import settings
from datetime import datetime

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Base(DeclarativeBase):
    id:Mapped[int]=mapped_column(primary_key=True, autoincrement=True,comment="主键ID")
    create_time:Mapped[datetime]=mapped_column(DateTime, comment="创建时间",default=datetime.now)
    update_time:Mapped[datetime]=mapped_column(DateTime, comment="更新时间",default=datetime.now,onupdate=datetime.now)
