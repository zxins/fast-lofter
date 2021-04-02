# -*- coding: utf-8 -*-
from fastapi import APIRouter, Path

from .controllers import PostCtrl

post_router = APIRouter(prefix='/posts')


@post_router.get('', summary="获取文章列表")
async def get_posts_list(page: int = 1, per_page: int = 10):
    pagination = PostCtrl().get_posts_paginate(page=page, per_page=per_page)

    return {
        "r": {
            "items": pagination.items,
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total_page": pagination.pages
        },
        "msg": "",
        "code": 0
    }


@post_router.get('/{post_id}', summary="查看文章详情")
async def get_post_detail(post_id: int = Path(...)):
    post = PostCtrl().get_one_post(post_id)
    return {
        "r": post or {},
        "msg": "",
        "code": 0
    }
