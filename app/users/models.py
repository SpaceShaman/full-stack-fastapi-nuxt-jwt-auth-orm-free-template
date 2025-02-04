from pydantic import BaseModel


class User(BaseModel):
    username: str
    is_active: bool


class UserWithPassword(User):
    password: str


class UserWithActivationCode(User):
    activation_code: str
