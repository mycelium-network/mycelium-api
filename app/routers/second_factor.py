from fastapi import APIRouter, Depends
from app.models import users
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