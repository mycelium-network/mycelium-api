import app.config as config

def getUsers():
    ## Currently a DB mockup
    return config.fake_users_db

def getUserOTPSecret(user:str):
    config_user = config.fake_otp_secret_db[user]
    return config_user["secret"]