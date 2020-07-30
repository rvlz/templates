from fastapi import Depends

from app.main.config import get_settings
from app.main.auth import verify_access_token
from app.main.exceptions import EmailNotVerifiedException


def get_current_user_email(verify=True):
    def _get_current_user_email(
        payload=Depends(verify_access_token), settings=Depends(get_settings),
    ):
        namespace = settings.AUTH0_CLAIMS_NAMESPACE
        email = payload.get(f"{namespace}/email")
        email_verified = payload.get(f"{namespace}/email_verified")
        if verify and not email_verified:
            raise EmailNotVerifiedException()
        return email

    return _get_current_user_email
