"""empty message

Revision ID: 2bcb2106b74f
Revises: 8d10112e501e
Create Date: 2021-11-30 14:45:14.493856

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2bcb2106b74f'
down_revision = '8d10112e501e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cargas_categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.Column('carga_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carga_id'], ['cargas.id'], ),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('caminhoes', sa.Column('placa', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'caminhoes', ['placa'])
    op.add_column('cargas', sa.Column('previsao_entrega', sa.String(), nullable=False))
    op.add_column('cargas', sa.Column('volume', sa.Float(), nullable=False))
    op.drop_column('cargas', 'peso')
    op.add_column('motoristas', sa.Column('cnh', sa.String(length=11), nullable=False))
    op.add_column('motoristas', sa.Column('updated_at', sa.DateTime(), nullable=True))
    op.add_column('motoristas', sa.Column('localizacao', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'motoristas', ['cnh'])
    op.add_column('usuarios', sa.Column('email', sa.String(), nullable=True))
    op.add_column('usuarios', sa.Column('celular', sa.String(), nullable=False))
    op.add_column('usuarios', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuarios', 'updated_at')
    op.drop_column('usuarios', 'celular')
    op.drop_column('usuarios', 'email')
    op.drop_constraint(None, 'motoristas', type_='unique')
    op.drop_column('motoristas', 'localizacao')
    op.drop_column('motoristas', 'updated_at')
    op.drop_column('motoristas', 'cnh')
    op.add_column('cargas', sa.Column('peso', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_column('cargas', 'volume')
    op.drop_column('cargas', 'previsao_entrega')
    op.drop_constraint(None, 'caminhoes', type_='unique')
    op.drop_column('caminhoes', 'placa')
    op.drop_table('cargas_categorias')
    op.drop_table('categorias')
    # ### end Alembic commands ###