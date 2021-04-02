# -*- coding: utf-8 -*-
from fastapi import FastAPI
from services.routers import router


def create_app():
    app = FastAPI(title="FastLofter")
    app.include_router(router)
    return app
