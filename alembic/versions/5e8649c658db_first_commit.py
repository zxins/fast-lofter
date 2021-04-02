"""first commit

Revision ID: 5e8649c658db
Revises: 
Create Date: 2021-04-02 11:51:15.680736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e8649c658db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('post_id', sa.BigInteger(), autoincrement=True, nullable=False, comment='文章id'),
    sa.Column('title', sa.String(length=125), nullable=False, comment='标题'),
    sa.Column('content', sa.Text(), nullable=False, comment='内容'),
    sa.Column('cover', sa.String(length=125), nullable=False, comment='封面'),
    sa.Column('published_at', sa.DateTime(), nullable=False, comment='发布时间'),
    sa.Column('is_hidden', sa.Boolean(), nullable=True, comment='是否隐藏'),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), nullable=False, comment='更新时间'),
    sa.PrimaryKeyConstraint('post_id'),
    sa.UniqueConstraint('title')
    )
    op.create_index(op.f('ix_post_created_at'), 'post', ['created_at'], unique=False)
    op.create_index(op.f('ix_post_published_at'), 'post', ['published_at'], unique=False)
    op.create_index(op.f('ix_post_updated_at'), 'post', ['updated_at'], unique=False)
    op.create_table('post_category',
    sa.Column('post_cid', sa.BigInteger(), autoincrement=True, nullable=False, comment='关系id'),
    sa.Column('post_id', sa.BigInteger(), nullable=False, comment='文章id'),
    sa.Column('category_id', sa.BigInteger(), nullable=False, comment='分类id'),
    sa.PrimaryKeyConstraint('post_cid')
    )
    op.create_table('post_tag',
    sa.Column('post_tid', sa.BigInteger(), autoincrement=True, nullable=False, comment='关系id'),
    sa.Column('post_id', sa.BigInteger(), nullable=False, comment='文章id'),
    sa.Column('tag_id', sa.BigInteger(), nullable=False, comment='标签id'),
    sa.PrimaryKeyConstraint('post_tid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tag')
    op.drop_table('post_category')
    op.drop_index(op.f('ix_post_updated_at'), table_name='post')
    op.drop_index(op.f('ix_post_published_at'), table_name='post')
    op.drop_index(op.f('ix_post_created_at'), table_name='post')
    op.drop_table('post')
    # ### end Alembic commands ###