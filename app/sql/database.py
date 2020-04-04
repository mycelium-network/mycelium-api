import app.config as config

def getUsers():
    ## Currently a DB mockup
    return config.fake_users_db

def getUserOTPSecret(user:str):
    return config.fake_otp_secret_db[user]