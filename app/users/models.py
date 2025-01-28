from pydantic import BaseModel


class UserWithPassword(BaseModel):
    username: str
    password: str
