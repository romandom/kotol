"""v_0.1

Revision ID: c84bf893ee4f
Revises: 
Create Date: 2023-02-09 17:10:35.419160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c84bf893ee4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('products',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipes',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('shared', sa.Boolean(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('decoction', sa.Boolean(), nullable=True),
    sa.Column('infusion', sa.Boolean(), nullable=True),
    sa.Column('info', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_recipes',
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('recipe_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'recipe_id')
    )
    op.create_table('fermentation',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('info', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('recipe_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('history',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(), nullable=True),
    sa.Column('recipe_id', postgresql.UUID(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('malt',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('degrees', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('amount', sa.String(), nullable=True),
    sa.Column('info', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('recipe_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mash',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('amount', sa.String(), nullable=True),
    sa.Column('info', sa.String(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('recipe_id', postgresql.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mash')
    op.drop_table('malt')
    op.drop_table('history')
    op.drop_table('fermentation')
    op.drop_table('favorite_recipes')
    op.drop_table('recipes')
    op.drop_table('products')
    op.drop_table('users')
    # ### end Alembic commands ###
