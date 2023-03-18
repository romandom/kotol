"""v_0.2

Revision ID: 0ccca9d3ac77
Revises: c84bf893ee4f
Create Date: 2023-02-11 17:21:28.682993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ccca9d3ac77'
down_revision = 'c84bf893ee4f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('name', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('beer_type', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('degrees', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('style', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('ibu', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('color', sa.String(), nullable=True))
    op.add_column('recipes', sa.Column('alcohol', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('recipes', 'alcohol')
    op.drop_column('recipes', 'color')
    op.drop_column('recipes', 'ibu')
    op.drop_column('recipes', 'style')
    op.drop_column('recipes', 'degrees')
    op.drop_column('recipes', 'beer_type')
    op.drop_column('recipes', 'name')
    # ### end Alembic commands ###