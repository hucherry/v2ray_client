"""v2ray_config

Revision ID: 5c9c1cd1380a
Revises: 
Create Date: 2019-09-07 12:05:07.853828

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c9c1cd1380a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscription',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('addr', sa.String(length=100), nullable=True),
    sa.Column('remarks', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('num')
    )
    op.create_table('v2ray_config',
    sa.Column('num', sa.Integer(), nullable=False),
    sa.Column('add', sa.String(length=100), nullable=True),
    sa.Column('host', sa.String(length=100), nullable=True),
    sa.Column('id', sa.String(length=100), nullable=True),
    sa.Column('aid', sa.Integer(), nullable=True),
    sa.Column('type', sa.String(length=100), nullable=True),
    sa.Column('net', sa.String(length=100), nullable=True),
    sa.Column('path', sa.String(length=100), nullable=True),
    sa.Column('ps', sa.String(length=100), nullable=True),
    sa.Column('tls', sa.String(length=20), nullable=True),
    sa.Column('port', sa.Integer(), nullable=True),
    sa.Column('mux', sa.String(length=20), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('sub', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('num')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('v2ray_config')
    op.drop_table('subscription')
    # ### end Alembic commands ###
