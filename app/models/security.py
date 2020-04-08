from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from passlib.context import CryptContext
import jwt

from app.models import users
import app.config as config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


class SecondFactorTokenIn(BaseModel):
    code: str = Field(
        ...,
        title="Security code for TOTP",
        min_length=6,
        max_length=6
    )


class SecondFactorTokenOut(BaseModel):
    code: str
    verified: bool


class SecondFactorQRCode(BaseModel):
    qrcode: str = Field(
        ...,
        title="Encode this value as a QR-Code and present the user for scanning.",
    )
    totp_secret: str = Field(
        ...,
        title="The shared secret for 2FA.",
    )
    username: str = Field(
        ...,
        title="Username of the user that enables the 2FA.",
    )


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(fake_db, username: str, password: str):
    user = users.get_user(fake_db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.PRIVATE_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt
