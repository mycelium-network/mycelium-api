from fastapi import Depends, FastAPI, Header, HTTPException

# Router Imports
from app.routers import items, users, second_factor, authentication
# Model Imports
# Configuration Import
import app.config as config

app = FastAPI(
    title = config.TITLE,
    description = config.DESCRIPTION,
    version = config.VERSION
)

# Authentication Routers
app.include_router(
    authentication.router,
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

# Authenticated APIs (prefix /auth)
app.include_router(
    second_factor.router,
    prefix="/auth",
    tags=["2-Factor Authentication"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    users.router,
    prefix="/auth",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    items.router,
    prefix="/auth",
    tags=["Items"],
    responses={404: {"description": "Not found"}},
)

# Unauthenticated APIs (prefix /public)