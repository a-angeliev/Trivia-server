"""empty message

Revision ID: 3d8d9ddec99f
Revises: e372adf82e7c
Create Date: 2022-08-16 20:12:56.344837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d8d9ddec99f'
down_revision = 'e372adf82e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('riddles', sa.Column('hint', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('riddles', 'hint')
    # ### end Alembic commands ###
