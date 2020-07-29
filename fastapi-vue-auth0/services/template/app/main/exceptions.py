from fastapi import Request
from fastapi.responses import JSONResponse


class AuthException(Exception):
    def __init__(self, code, description, status_code=401):
        self.status_code = status_code
        self.code = code
        self.description = description


def auth_exception_handler(request: Request, exc: AuthException):
    return JSONResponse(
        status_code=exc.status_code,
        content=dict(
            code=exc.code,
            description=exc.description,
        ),
    )


class EmailTakenException(Exception):
    pass


def email_taken_exception_handler(request: Request, exc: EmailTakenException):
    return JSONResponse(
        status_code=403,
        content=dict(
            code="email_taken",
            description="Email already taken.",
        ),
    )


class EmailNotVerifiedException(Exception):
    pass


def email_not_verified_exception_handler(
    request: Request,
    exc: EmailNotVerifiedException
):
    return JSONResponse(
        status_code=403,
        content=dict(
            code="email_not_verified",
            description="Email verification required.",
        ),
    )


class UserNotFoundException(Exception):
    pass


def user_not_found_exception_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content=dict(
            code="user_not_found",
            description="User not found."
        )
    )
