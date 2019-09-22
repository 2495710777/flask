"""创建empmanager表

Revision ID: a2816ba5a936
Revises: 
Create Date: 2019-09-22 15:51:18.648666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2816ba5a936'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emp',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('pwd', sa.String(length=32), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('sex', sa.String(length=8), nullable=True),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('ask', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emp')
    # ### end Alembic commands ###
