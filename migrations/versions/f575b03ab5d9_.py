"""empty message

Revision ID: f575b03ab5d9
Revises: 68862d03e88a
Create Date: 2020-12-21 20:10:12.448846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f575b03ab5d9'
down_revision = '68862d03e88a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=94), nullable=True),
    sa.Column('is_staff', sa.Boolean(), nullable=True),
    sa.Column('uuid', sa.String(length=36), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('login', name=op.f('uq_user_login')),
    sa.UniqueConstraint('uuid', name=op.f('uq_user_uuid'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
