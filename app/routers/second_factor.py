from fastapi import APIRouter, Depends, Body, HTTPException
from app.models import users, security
from app.sql import database
import app.config as config
import pyotp

router = APIRouter()


@router.get(
    "/2fa/status",
    summary="Status of the 2FA configuration"
)
def status(current_user: users.User = Depends(users.get_current_active_user)):
    """
    Get information if the current user has the second factor enabled.
    """
    return {"status": current_user.second_factor}

@router.post(
    "/2fa/verify",
    summary="Verify with the 2FA",
    response_model=security.SecondFactorTokenOut
)
def verify(*,
    code: security.SecondFactorTokenIn,
    current_user: users.User = Depends(users.get_current_active_user)):
    """
    Verify the authorization with security code generate by TOTP.
    """
    if current_user.second_factor:
        code = code.code
        user_totp_secret = database.getUserOTPSecret(current_user.username)
        totp = pyotp.TOTP(user_totp_secret)
        if totp.verify(code):
            return {"code":code,"verified":True}
        else:
            return {"code":code,"verified":False}
    else:
        raise HTTPException(status_code=404, detail="Second Factor not found")