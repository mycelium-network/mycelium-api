# APPLICATION CONFIG
TITLE = "Mycelium-Network API"
DESCRIPTION = """
__ALPHA STATUS__

Mycelium is a distributed network to share common goods.

Find the full project under https://www.mycelium.space/.

A live version of the API is hosted under https://mycelium-api.herokuapp.com/docs.

#### Demo Users
| User | Password | TOTP Secret |
|---|---|---|
|johndoe|secret|PD6D3NQ3CKVEPIHH|
|alice|secret|Q5XR4DG5KASPGWNA|
|bob|secret|XLQAFA3YDIHHEZWB|
"""
VERSION = "0.0.1.alpha"
APPLICATION_NAME = "Mycelium Network"
APPLICATION_URL = "mycelium-api.herokuapp.com"


# SECURITY RELEVANT CONFIGURATION!
# !DANGER
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7" # openssl rand -hex 32
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# TEMPORARY CONSTANTS
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", # secret
        "disabled": False,
        "second_factor": False
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", # secret
        "disabled": True,
        "second_factor": False
    },
    "bob": {
        "username": "bob",
        "full_name": "Bob",
        "email": "bob@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW", # secret
        "disabled": False,
        "second_factor": True
    }
}

fake_otp_secret_db = {
    "johndoe": {
        "secret" : "PD6D3NQ3CKVEPIHH"
    },
    "alice": {
        "secret" : "Q5XR4DG5KASPGWNA"
    },
    "bob": {
        "secret" : "XLQAFA3YDIHHEZWB"
    }
}
