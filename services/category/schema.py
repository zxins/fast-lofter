# -*- coding: utf-8 -*-
from pydantic import BaseModel

class CategoryRespModel(BaseModel):
    category_id: int
    name: str