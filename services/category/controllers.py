# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import select, insert

from lib.controller import BaseCtrl
from lib.db_paginate import Pagination
from services.category.models import CategoryDBModel
from services.category.schema import CategoryRespModel


class CategoryCtrl(BaseCtrl):

    def create_category(self, name: str):
        q = insert(CategoryDBModel).values(name=name, created_at=datetime.now())
        self.db.execute(q)
        self.__commit__()

    def get_category_paginate(self, per_page: int, page: int, filters=(), orders=()) -> Pagination:
        return self._get_paginate(CategoryDBModel, CategoryRespModel, per_page, page, filters, orders)

    def get_one_category(self, category_id: int):
        q = select(CategoryDBModel).where(CategoryDBModel.category_id == category_id)
        category = self.db.execute(q).scalar_one_or_none()
        return CategoryRespModel.from_orm(category) if category else category
