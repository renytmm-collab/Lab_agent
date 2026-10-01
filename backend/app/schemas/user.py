from pydantic import BaseModel,ConfigDict

class UserResponse(BaseModel):
    id: int
    username: str
    name: str
    role: str
    email:  str | None=None
    phone: str | None=None
    status:int

    model_config=ConfigDict(from_attributes=True)
