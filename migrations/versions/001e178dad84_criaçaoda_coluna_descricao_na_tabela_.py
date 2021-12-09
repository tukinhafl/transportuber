"""Criaçaoda coluna descricao na tabela cargas

Revision ID: 001e178dad84
Revises: 18a1a0d39e36
Create Date: 2021-12-08 13:18:42.425912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001e178dad84'
down_revision = '18a1a0d39e36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cargas', sa.Column('descricao', sa.String(), nullable=True))
    op.alter_column('cargas', 'destino',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cargas', 'destino',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('cargas', 'descricao')
    # ### end Alembic commands ###
