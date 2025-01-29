import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


users_router = APIRouter(prefix="/users", tags=["users"])


@users_router.get("/me")
async def get_me(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, "test", algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"username": payload["sub"]}
