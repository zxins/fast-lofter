# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, Boolean, BigInteger

from database import Base


class PostDBModel(Base):
    """ 文章 """

    __tablename__ = 'post'

    post_id = Column(BigInteger, primary_key=True, autoincrement=True, comment="文章id")
    category_id = Column(BigInteger, nullable=True, comment="分类id")

    # author = Column(String(35), nullable=False, default="", comment="作者")  # 暂不关联用户
    title = Column(String(125), unique=True, nullable=False, default="", comment="标题")
    content = Column(Text, nullable=False, default="", comment="内容")
    cover = Column(String(125), nullable=False, default="", comment="封面")
    published_at = Column(DateTime, nullable=False, index=True, comment="发布时间")
    is_hidden = Column(Boolean, default=True, comment="是否隐藏")
    created_at = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="创建时间")
    updated_at = Column(DateTime, default=datetime.now, nullable=False, index=True, comment="更新时间")


class PostTagDBModel(Base):
    """ 文章标签关系 """

    __tablename__ = 'post_tag'

    post_tid = Column(BigInteger, primary_key=True, autoincrement=True, comment="关系id")
    post_id = Column(BigInteger, nullable=False, index=True, comment="文章id")
    tag_id = Column(BigInteger, nullable=False, index=True, comment="标签id")
