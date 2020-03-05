"""add groups

Revision ID: f28c3fd2a06f
Revises: 59055cc1934f
Create Date: 2020-03-05 11:10:05.951923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f28c3fd2a06f'
down_revision = '59055cc1934f'
branch_labels = ()
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sample_set', sa.Column('groups', sa.String(), nullable=True), schema='sample_db')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sample_set', 'groups', schema='sample_db')
    # ### end Alembic commands ###
