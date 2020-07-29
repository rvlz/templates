from typing import Optional

import requests
from fastapi import Header, Depends
from jose import jwt
from jose.exceptions import JWTError

from .config import get_settings
from .exceptions import AuthException


def get_auth_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise AuthException(
            code="authorization_header_missing",
            description="Authorization header expected.",
        )
    parts = authorization.split()
    if len(parts) != 2:
        raise AuthException(
            code="invalid_header", description="Invalid authorization header.",
        )
    if parts[0].lower() != "bearer":
        raise AuthException(
            code="invalid_header",
            description="Authorization header must start with Bearer.",
        )
    return parts[1]


def fetch_jwks(settings=Depends(get_settings)):
    url = f"https://{settings.AUTH0_DOMAIN}/.well-known/jwks.json"
    jwks = requests.get(url).json()
    return jwks


def verify_access_token(
    token: str = Depends(get_auth_token),
    jwks=Depends(fetch_jwks),
    settings=Depends(get_settings),
):
    rsa_key = {}
    try:
        unverified_header = jwt.get_unverified_header(token)
    except JWTError:
        raise AuthException(
            code="invalid_token", description="Invalid access token."
        )
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"],
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=settings.AUTH0_ALGORITHMS,
                audience=settings.AUTH0_API_AUDIENCE,
                issuer=f"https://{settings.AUTH0_DOMAIN}/",
            )
        except jwt.ExpiredSignatureError:
            raise AuthException(
                code="token_expired", description="Token expired.",
            )
        except jwt.JWTClaimsError:
            raise AuthException(
                code="invalid_claims", description="Incorrect claims.",
            )
        except Exception:
            raise AuthException(
                code="invalid_header", description="Authentication failure.",
            )
        return payload
    raise AuthException(
        code="invalid_header", description="Unable to find appropriate key.",
    )


def verify_scope(required_scope):
    def _verify_scope(token: str = Depends(get_auth_token)):
        claims = jwt.get_unverified_claims(token)
        scope = claims.get("scope")
        if scope:
            token_scopes = scope.split()
            for ts in token_scopes:
                if ts == required_scope:
                    return True
        raise AuthException(
            code="missing_authorization", description="Authorization failure",
        )

    return _verify_scope
