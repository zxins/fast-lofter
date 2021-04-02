# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger

from database import Base


class CategoryDBModel(Base):
    """ 分类 """

    __tablename__ = 'category'

    category_id = Column(BigInteger, primary_key=True, autoincrement=True, comment="分类id")
    name = Column(String(25), nullable=False, comment="分类名")
    created_at = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
