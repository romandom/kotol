"""v0.2

Revision ID: 47325177e45e
Revises: f5fb5f41b844
Create Date: 2023-04-11 22:34:40.376926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47325177e45e'
down_revision = 'f5fb5f41b844'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('temperature', sa.String(), nullable=True))
    op.add_column('temperatures', sa.Column('time', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('temperatures', 'time')
    op.drop_column('products', 'temperature')
    # ### end Alembic commands ###
