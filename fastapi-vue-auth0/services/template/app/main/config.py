import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str
    SECRET_KEY: str
    VERSION: str
    AUTH0_DOMAIN: str
    AUTH0_API_AUDIENCE: str
    AUTH0_ALGORITHMS: List[str]
    AUTH0_CLAIMS_NAMESPACE: str


class DevelopmentSettings(CommonSettings):
    DATABASE_URL: str


class TestSettings(CommonSettings):
    DATABASE_URL: str

    class Config:
        fields = {"DATABASE_URL": {"env": "DATABASE_TEST_URL"}}


class StagingSettings(CommonSettings):
    DATABASE_URL: str


class ProductionSettings(CommonSettings):
    DATABASE_URL: str


def select_settings(environment="development"):
    settings = {
        "development": DevelopmentSettings,
        "test": TestSettings,
        "staging": StagingSettings,
        "production": ProductionSettings,
    }
    return settings[environment]()


@lru_cache
def get_settings():
    environment = os.getenv("APP_ENV", "development")
    return select_settings(environment)
