from pydantic import BaseModel


class User(BaseModel):
    username: str
    is_active: bool


class UserWithPassword(BaseModel):
    username: str
    password: str
