# -*- coding: utf-8 -*-
from sqlalchemy import select, insert

from library.controller import BaseCtrl
from library.db_paginate import Pagination
from services.tag.models import TagDBModel
from services.tag.schema import TagRespModel


class TagCtrl(BaseCtrl):

    def create_tag(self, name: str):
        q = insert(TagDBModel).values(name=name)
        self.db.execute(q)
        self.__commit__()

    def get_tag_paginate(self, per_page: int, page: int, filters=(), orders=()) -> Pagination:
        return self._get_paginate(TagDBModel, TagRespModel, per_page, page, filters, orders)

    def get_one_tag(self, tag_id: int):
        q = select(TagDBModel).where(TagDBModel.tag_id == tag_id)
        tag = self.db.execute(q).scalar_one_or_none()
        return TagRespModel.from_orm(tag) if tag else tag
