"""empty message

Revision ID: 814522b75445
Revises: 
Create Date: 2019-11-16 20:21:40.365444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814522b75445'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('role', sa.String(length=30), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('apps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('document', sa.String(length=50), nullable=False),
    sa.Column('image', sa.Text(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('document'),
    sa.UniqueConstraint('owner_id')
    )
    op.create_table('addresss',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=128), nullable=False),
    sa.Column('city', sa.Integer(), nullable=False),
    sa.Column('zipCode', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=128), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['entity_id'], ['entities.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('entityApps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('app_id', sa.Integer(), nullable=False),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('entity', sa.Integer(), nullable=False),
    sa.Column('app', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['app'], ['apps.id'], ),
    sa.ForeignKeyConstraint(['entity'], ['entities.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('career', sa.String(length=128), nullable=False),
    sa.Column('birthDate', sa.Date(), nullable=False),
    sa.Column('sex', sa.String(length=20), nullable=False),
    sa.Column('telephone', sa.Integer(), nullable=False),
    sa.Column('married', sa.Boolean(), nullable=True),
    sa.Column('cpf', sa.Integer(), nullable=True),
    sa.Column('rg', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('modified_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_app', sa.Integer(), nullable=True),
    sa.Column('created_app', sa.Integer(), nullable=True),
    sa.Column('modified_app', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['entity_id'], ['entities.id'], ),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('entityApps')
    op.drop_table('addresss')
    op.drop_table('entities')
    op.drop_table('apps')
    op.drop_table('users')
    # ### end Alembic commands ###
