# -*- coding: utf-8 -*-
from fastapi import APIRouter, Path

from .controllers import TagCtrl
from ..post.controllers import PostCtrl

tag_router = APIRouter(prefix='/tags')


@tag_router.get('')
def get_tag_list(page: int = 1, per_page: int = 10):
    pagination = TagCtrl().get_tag_paginate(page=page, per_page=per_page)
    return {
        "r": {
            "tags": pagination.items,
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total_page": pagination.pages,
        },
        "msg": "",
        "code": 0
    }


@tag_router.get('/{tag_id}/posts')
def get_tag_posts(tag_id: int = Path(...), page: int = 1, per_page: int = 10):
    pagination = PostCtrl().get_posts_paginate_by_tag(tag_id, page=page, per_page=per_page)
    return {
        "r": {
            "posts": pagination.items,
            "per_page": pagination.per_page,
            "page": pagination.page,
            "total_page": pagination.pages
        }
    }
