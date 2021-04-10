# -*- coding: utf-8 -*-
from typing import Optional, Any

from sqlalchemy import select
from sqlalchemy.orm import Session

from database import SessionLocal, Base
from library.db_paginate import Pagination


class BaseCtrl:
    def __init__(self, db: Optional[Session] = None):
        self.db = db or SessionLocal()
        if db is None:
            self.is_local_db = True
        else:
            self.is_local_db = False

    def __del__(self):
        try:
            if self.is_local_db:
                self.db.close()
        except:
            pass

    def __commit__(self):
        """提交
        谁创建(db, 事务)，谁提交
        """
        try:
            if self.is_local_db:
                self.db.commit()
        except:
            pass

    def _get_paginate(self, model: Base, items_schema: Any, per_page: int, page: int, filters: tuple = (),
                      orders: tuple = ()) -> Pagination:
        """分页查询
        :param model: 数据表反射model
        :param items_schema: 结果集的单个元素schema
        :param per_page: 每页多少rows
        :param page: 当前页数
        :param filters: 查询条件
        :param orders: 排序条件
        :return: 分页对象Pagination()
        """

        # 查询语句
        q = select(model).where(*filters).order_by(*orders)

        # 分页查询结果
        items = self.db.execute(
            q.limit(per_page).offset((page - 1) * per_page)
        ).scalars().all()

        # 满足该条件的总行数
        total = self.db.execute(
            q.order_by(None)
        ).raw.rowcount

        # 通过schema输出items
        out_items = [items_schema.from_orm(item) for item in items]

        # 返回分页对象
        return Pagination(page, per_page, total, out_items, None)
