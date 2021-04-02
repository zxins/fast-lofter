# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class PostRespModel(BaseModel):
    post_id: int
    title: str
    content: str
    cover: str
    published_at: datetime

    class Config:
        orm_mode = True


class PostCreateModel(BaseModel):
    title: str
    content: str
    cover: str
    published_at: datetime = datetime.now()
    category_id: Optional[int]
    tag_ids: set = ()
