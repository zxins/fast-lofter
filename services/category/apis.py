# -*- coding: utf-8 -*-
from fastapi import APIRouter
from .controllers import CategoryCtrl

category_router = APIRouter(prefix='/category')


@category_router.get('')
def get_category_list(page: int = 1, per_page: int = 10):
    pagination = CategoryCtrl().get_category_paginate(page=page, per_page=per_page)
    return {
        "r": {
            "categories": pagination.items,
            "page": pagination.page,
            "per_page": pagination.per_page,
            "total_page": pagination.pages,
        },
        "msg": "",
        "code": 0
    }
