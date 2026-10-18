from fastapi import FastAPI
from app.model.user import User
from app.database import Base,engine
from app.api import api
from app.common.exception import (
    BusinessException, business_exception_handler,
    HTTPException, http_business_exception_handler,
    RequestValidationError, vallidation_exception_handler, global_exception_handler
)

Base.metadata.create_all(bind=engine)

app=FastAPI()
app.add_exception_handler(BusinessException, business_exception_handler)
app.add_exception_handler(HTTPException, http_business_exception_handler)
app.add_exception_handler(RequestValidationError, vallidation_exception_handler)
app.add_exception_handler(Exception,global_exception_handler)
app.include_router(api)

@app.get("/")
def root():
    return  {"message": "Hello, World!"}
