import app.config as config


def get_users():
    # Currently a DB mockup
    return config.fake_users_db


def get_user_otp_secret(user: str):
    config_user = config.fake_otp_secret_db[user]
    return config_user["secret"]
