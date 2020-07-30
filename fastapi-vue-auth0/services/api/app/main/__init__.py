import os

from fastapi import FastAPI

from .api.ping import router as ping_router
from .api.user import router as user_router
from .exceptions import (
    AuthException,
    auth_exception_handler,
    EmailTakenException,
    email_taken_exception_handler,
    EmailNotVerifiedException,
    email_not_verified_exception_handler,
    UserNotFoundException,
    user_not_found_exception_handler,
)


def create_app():
    app = FastAPI()
    register_routers(app)
    register_exception_handlers(app)
    return app


def register_routers(app):
    version = os.getenv("VERSION")
    app.include_router(ping_router, prefix=f"/api/{version}/ping")
    app.include_router(user_router, prefix=f"/api/{version}/users")


def register_exception_handlers(app):
    app.exception_handler(AuthException)(auth_exception_handler)
    app.exception_handler(EmailTakenException)(email_taken_exception_handler)
    app.exception_handler(EmailNotVerifiedException)(
        email_not_verified_exception_handler
    )
    app.exception_handler(UserNotFoundException)(
        user_not_found_exception_handler
    )
