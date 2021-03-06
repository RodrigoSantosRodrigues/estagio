"""empty message

Revision ID: 2af8295ff27e
Revises: c276fddee0c0
Create Date: 2019-11-16 21:21:45.356679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2af8295ff27e'
down_revision = 'c276fddee0c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('entityApps_entity_fkey', 'entityApps', type_='foreignkey')
    op.drop_constraint('entityApps_app_fkey', 'entityApps', type_='foreignkey')
    op.create_foreign_key(None, 'entityApps', 'apps', ['app_id'], ['id'])
    op.create_foreign_key(None, 'entityApps', 'entities', ['entity_id'], ['id'])
    op.drop_column('entityApps', 'app')
    op.drop_column('entityApps', 'entity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('entityApps', sa.Column('entity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('entityApps', sa.Column('app', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'entityApps', type_='foreignkey')
    op.drop_constraint(None, 'entityApps', type_='foreignkey')
    op.create_foreign_key('entityApps_app_fkey', 'entityApps', 'apps', ['app'], ['id'])
    op.create_foreign_key('entityApps_entity_fkey', 'entityApps', 'entities', ['entity'], ['id'])
    # ### end Alembic commands ###
