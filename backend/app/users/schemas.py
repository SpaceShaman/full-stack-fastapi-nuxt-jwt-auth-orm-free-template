from pydantic import BaseModel


class User(BaseModel):
    username: str
    is_active: bool
    password: str | None = None
    email: str | None = None
    activation_code: str | None = None
