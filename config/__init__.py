import os
from typing import Union, Optional

from pydantic import BaseSettings, AnyHttpUrl, IPvAnyAddress
from pydantic.dataclasses import dataclass


class Config(BaseSettings):
    # 项目目录 - 当前文件所在上级目录
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # 文档
    DOCS_URL: str = "/docs"
    OPENAPI_URL: str = "/openapi.json"
    REDOC_URL: Optional[str] = "/redoc"

    # Debug
    DEBUG_APP_KEYS: list = ["abcdefghijklmnopqrstuvwxyz"]

    # token
    ACCESS_TOKEN_EXPIRE_DAYS: int = 10
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = 'aeq)s(*&dWEQasd8**&^9asda_asdasd*&*&^+_sda'

    # MySQL
    MYSQL_USER: str = "root"
    MYSQL_PASS: str = os.environ['MYSQL_PASS']
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_DATABASE: str = "lofter"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # Redis
    REDIS_HOST: str = "127.0.0.1"
    REDIS_PORT: int = 6379
    REDIS_PASS: str = ""

    # cache
    REDIS_CACHE_DB: int = 0
    CACHE_PREFIX: str = "lofter"


config = Config()
