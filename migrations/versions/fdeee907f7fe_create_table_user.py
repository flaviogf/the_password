"""create table user

Revision ID: fdeee907f7fe
Revises: 
Create Date: 2019-07-28 17:02:54.736037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdeee907f7fe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
                    sa.Column('id',
                              sa.Integer,
                              primary_key=True),
                    sa.Column('name',
                              sa.String(250),
                              nullable=False),
                    sa.Column('email',
                              sa.String(250),
                              nullable=False),
                    sa.Column('password',
                              sa.String(250),
                              nullable=False))


def downgrade():
    op.drop_table('user')
