"""empty message

Revision ID: ccb4e5a353ff
Revises: 04a21f4d08b7
Create Date: 2021-11-30 17:11:59.759066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb4e5a353ff'
down_revision = '04a21f4d08b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('cargas_dono_id_key', 'cargas', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('cargas_dono_id_key', 'cargas', ['dono_id'])
    # ### end Alembic commands ###