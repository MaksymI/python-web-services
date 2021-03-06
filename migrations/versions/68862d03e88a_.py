"""empty message

Revision ID: 68862d03e88a
Revises: 
Create Date: 2020-12-20 20:26:14.067616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68862d03e88a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_post')),
    sa.UniqueConstraint('uuid', name=op.f('uq_post_uuid'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
