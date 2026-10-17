from fastapi import APIRouter, Depends
from app.api.auth import router as auth_router
from app.api.user import router as user_router

api=APIRouter(prefix="/api")

api.include_router(auth_router)
api.include_router(user_router)