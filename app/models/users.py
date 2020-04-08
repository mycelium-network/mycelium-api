from pydantic import BaseModel
import jwt
from jwt import PyJWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.models import security
from app.sql import database
import app.config as config


class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None
    disabled: bool = None
    second_factor: bool = False


class UserInDB(User):
    username: str
    hashed_password: str


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)
    raise HTTPException(status_code=404, detail="User not found.")


async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.PUBLIC_KEY,
                             algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = security.TokenData(username=username)
    except PyJWTError:
        raise credentials_exception
    user = get_user(database.get_users(), username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
