# -*- coding: utf-8 -*-
from pydantic import BaseModel


class TagRespModel(BaseModel):
    tag_id: int
    name: str

    class Config:
        orm_mode = True
