from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def generate_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def check_password_strength(password: str) -> bool:
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if all((char.isalnum() for char in password)):
        return False
    return any((char.islower() for char in password))
