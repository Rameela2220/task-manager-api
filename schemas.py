from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class Login(BaseModel):
    email: str
    password: str


class TaskCreate(BaseModel):
    title: str
    description: str