from fastapi import APIRouter, Depends, HTTPException
import pyotp

from app.models import users, security
from app.sql import database
import app.config as config


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
        user_totp_secret = database.get_user_otp_secret(current_user.username)
        totp = pyotp.TOTP(user_totp_secret)
        if totp.verify(code):
            return {"code": code, "verified": True}
        return {"code": code, "verified": False}
    raise HTTPException(status_code=404, detail="Second Factor not found")


@router.get(
    "/2fa/enable",
    summary="Enable and create a new 2FA config",
    response_model=security.SecondFactorQRCode
)
def enable(current_user: users.User = Depends(users.get_current_active_user)):
    """
    Enable the 2FA process and will return an string containing
    the value typically presented as a QR-Code.
    """
    if not current_user.second_factor:
        totp_secret = pyotp.random_base32()
        qrcode = pyotp.totp.TOTP(totp_secret).provisioning_uri(
            current_user.username, config.APPLICATION_NAME+" - "+config.APPLICATION_URL)
        return {"qrcode": qrcode, "totp_secret": totp_secret, "username": current_user.username}
    raise HTTPException(status_code=401, detail="Second Factor already enabled")
