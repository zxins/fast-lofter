# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger

from database import Base


class TagDBModel(Base):
    """ 标签 """

    __tablename__ = 'tag'

    tag_id = Column(BigInteger, primary_key=True, autoincrement=True, comment="标签id")
    name = Column(String(25), nullable=False, comment="标签名")
    created_at = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
