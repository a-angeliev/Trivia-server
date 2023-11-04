"""empty message

Revision ID: a9612a3343d5
Revises: c7d8be7ecb4f
Create Date: 2022-08-14 23:48:16.441948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a9612a3343d5"
down_revision = "c7d8be7ecb4f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("events", sa.Column("guessed_answer", sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("events", "guessed_answer")
    # ### end Alembic commands ###
