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

# This name will be used to populate the SSL certificate as well.
# Can include your hackerspace or other group name but should be
# something that can be recognized in the public.
ORGANIZATION_UNIT = "Mycelium Network Project"


# SECURITY RELEVANT CONFIGURATION!
# !DANGER!
# Certificates will be generate newly on each restart.
CERT_FILE = "app/certificates/server_jwt_cert.pem"
PRIVATE_KEY_FILE = "app/certificates/server_jwt_private.key"
PUBLIC_KEY_FILE = "app/certificates/server_jwt_public.key"
CERT = ""
PRIVATE_KEY = ""
PUBLIC_KEY = ""

ALGORITHM = "RS512"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# TEMPORARY CONSTANTS
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
        "second_factor": False
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice",
        "email": "alice@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": True,
        "second_factor": False
    },
    "bob": {
        "username": "bob",
        "full_name": "Bob",
        "email": "bob@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
        "disabled": False,
        "second_factor": True
    }
}

fake_otp_secret_db = {
    "johndoe": {
        "secret": "PD6D3NQ3CKVEPIHH"
    },
    "alice": {
        "secret": "Q5XR4DG5KASPGWNA"
    },
    "bob": {
        "secret": "XLQAFA3YDIHHEZWB"
    }
}
