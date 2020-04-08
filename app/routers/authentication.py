from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm, OpenIdConnect
from app.models import security
from app.sql import database
import app.config as config

router = APIRouter()


@router.post("/token", response_model=security.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = security.authenticate_user(
        database.get_users(), form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/openid-connect", response_model=security.Token)
async def login_openid_connect(form_data: OpenIdConnect = Depends()):
    return {"status": ""}
