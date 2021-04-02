# -*- coding: utf-8 -*-
from fastapi import APIRouter

from .post.apis import post_router
from .tag.api import tag_router

router = APIRouter()
router.include_router(post_router, tags=["Post"])
router.include_router(tag_router, tags=["Tag"])