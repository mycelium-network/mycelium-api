from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.certificates import helper

# Router Imports
from app.routers import things, users, second_factor, authentication, autocomplete
# Model Imports
# Configuration Import
import app.config as config

# Generate a new Key Pair.
config.CERT, config.PRIVATE_KEY, config.PUBLIC_KEY = helper.create_self_signed_cert()

app = FastAPI(
    title=config.TITLE,
    description=config.DESCRIPTION,
    version=config.VERSION
)

# Configure CORS
origins = [
    "https://www.mycelium.space",
    "https://mycelium.space",
    "http://localhost:9000"  # Allows local frontend development for the public api
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Provide info for the api


@app.get(
    "/",
    tags=["Public"]
)
async def get_root_path():
    return {
        "status": "running",
        "swagger_ui": "/docs",
        "redoc": "/redoc",
        "openid_connect": "/.well-known/openid-configuration"
    }

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
    things.router,
    prefix="/auth",
    tags=["Things"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    autocomplete.router,
    prefix="/auth",
    tags=["Auto-Complete"],
    responses={404: {"description": "Not found"}},
)


# Unauthenticated APIs (prefix /public)
