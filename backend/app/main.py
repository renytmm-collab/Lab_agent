from fastapi import FastAPI
from app.model.user import User
from app.database import Base,engine
from app.api import api
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.common.exception import (
    BusinessException, business_exception_handler,
    http_business_exception_handler,
    RequestValidationError, validation_exception_handler, global_exception_handler
)


Base.metadata.create_all(bind=engine)

app=FastAPI()

origins=[
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(api)

app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(StarletteHTTPException, http_business_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception,global_exception_handler)

@app.get("/")
def root():
    return  {"message": "Hello, World!"}
