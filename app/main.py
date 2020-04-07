from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
async def root():
    return {
        "status": "running",
        "swagger_ui": "/docs",
        "redoc": "/redoc",
        "openid_connect": "/.well-known/openid-configuration"
        }

# Configure CORS
origins = [
    "https://www.mycelium.space",
    "http://localhost:9000" # Allows local frontend development for the public api
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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