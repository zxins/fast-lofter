# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional

from sqlalchemy import select, desc, insert

from database import MySQLSession
from lib.controller import BaseCtrl
from lib.db_paginate import Pagination
from services.post.models import PostDBModel, PostTagDBModel
from services.post.schemas import PostRespModel, PostCreateModel


class PostCtrl(BaseCtrl):

    def get_posts_paginate(self, per_page: int, page: int, filters=(), orders=(desc('created_at'),)) -> Pagination:
        return self._get_paginate(PostDBModel, PostRespModel, per_page, page, filters, orders)

    def get_one_post(self, post_id: int) -> PostRespModel:
        q = select(PostDBModel).where(
            PostDBModel.post_id == post_id,
            PostDBModel.is_hidden == False,
        )
        post = self.db.execute(q).scalar_one_or_none()
        return PostRespModel.from_orm(post) if post else post

    def get_posts_paginate_by_tag(self, tag_id: int, per_page: int, page: int):
        q = select(
            PostDBModel
        ).join(
            PostTagDBModel,
            PostTagDBModel.post_id == PostDBModel.post_id
        ).where(
            PostTagDBModel.tag_id == tag_id
        )

        # 分页查询结果
        posts = self.db.execute(
            q.limit(per_page).offset((page - 1) * per_page)
        ).scalars().all()

        # 满足该条件的总行数
        total = self.db.execute(
            q.order_by(None)
        ).raw.rowcount

        # 通过schema输出items
        items = [PostRespModel.from_orm(post) for post in posts]

        # 返回分页对象
        return Pagination(page, per_page, total, items, None)

    def create_post(self, post: PostCreateModel):
        with MySQLSession() as db:
            insert_post_q = insert(PostDBModel).values(
                category_id=post.category_id,
                title=post.title,
                content=post.content,
                cover=post.cover,
                published_at=post.published_at,
                is_hidden=False if post.published_at <= datetime.now() else True
            )
            insert_post_result = db.session.execute(insert_post_q)
            post_id = insert_post_result.inserted_primary_key[0]

            for tag_id in post.tag_ids:
                insert_post_tag_q = insert(PostTagDBModel).values(
                    tag_id=tag_id,
                    post_id=post_id
                )
                db.session.execute(insert_post_tag_q)

            db.session.commit()

            return post_id


if __name__ == '__main__':
    params = dict(
        title="测试标题5",
        content="的罚款是劳动法金坷垃圣诞节饭四等奖佛爱是否点击哦描述的减肥",
        cover="",
        category_id=11,
        tag_ids=(3,)
    )
    post = PostCreateModel(**params)

    ctrl = PostCtrl()
    ctrl.create_post(post)
    # posts = ctrl.get_posts_by_tag(2)
    # print(posts)
