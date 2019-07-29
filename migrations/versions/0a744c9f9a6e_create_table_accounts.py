"""create table accounts

Revision ID: 0a744c9f9a6e
Revises: fdeee907f7fe
Create Date: 2019-07-29 14:51:47.863033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a744c9f9a6e'
down_revision = 'fdeee907f7fe'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('accounts',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('login',
                              sa.String(250),
                              nullable=False),
                    sa.Column('password',
                              sa.String(250),
                              nullable=False),
                    sa.Column('user_id',
                              sa.Integer,
                              sa.ForeignKey('user.id')))


def downgrade():
    op.drop_table('accounts')
