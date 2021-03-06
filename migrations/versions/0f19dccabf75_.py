"""empty message

Revision ID: 0f19dccabf75
Revises: f575b03ab5d9
Create Date: 2020-12-25 18:40:07.589754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f19dccabf75'
down_revision = 'f575b03ab5d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_post_author_id_user'), 'post', 'user', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_post_author_id_user'), 'post', type_='foreignkey')
    op.drop_column('post', 'author_id')
    # ### end Alembic commands ###
