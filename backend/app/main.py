from fastapi import FastAPI
from app.model.user import User
from app.database import Base,engine
from app.api.auth import router as auth_router
from app.api import api

Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(api)

@app.get("/")
def root():
    return  {"message": "Hello, World!"}
