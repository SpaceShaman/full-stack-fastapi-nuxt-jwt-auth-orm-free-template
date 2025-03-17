from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class RegistrationSchema(BaseModel):
    username: str
    password: str
    email: str


class Credentials(BaseModel):
    username: str
    password: str


class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


class RecoverPasswordSchema(BaseModel):
    email: str
