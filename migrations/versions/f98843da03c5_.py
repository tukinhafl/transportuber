"""empty message

Revision ID: f98843da03c5
Revises: 
Create Date: 2021-12-14 22:15:38.009398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f98843da03c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('estados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('codigo_uf', sa.Integer(), nullable=False),
    sa.Column('uf', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('motoristas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sobrenome', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('celular', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('cnh', sa.String(length=11), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('localizacao', sa.String(), nullable=True),
    sa.Column('motorista_ativo', sa.Boolean(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('celular'),
    sa.UniqueConstraint('cnh'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('municipios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('latitude', sa.String(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.Column('codigo_uf', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('sobrenome', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('celular', sa.String(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('usuario_ativo', sa.Boolean(), nullable=True),
    sa.Column('super_adm', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('celular'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('avaliacoes_usuario_motorista',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nota', sa.Float(), nullable=False),
    sa.Column('motorista_id', sa.Integer(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['motorista_id'], ['motoristas.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('motorista_id'),
    sa.UniqueConstraint('usuario_id')
    )
    op.create_table('caminhoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(), nullable=False),
    sa.Column('modelo', sa.String(), nullable=False),
    sa.Column('capacidade_de_carga', sa.Float(), nullable=False),
    sa.Column('placa', sa.String(), nullable=False),
    sa.Column('motorista_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['motorista_id'], ['motoristas.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('placa')
    )
    op.create_table('cargas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('disponivel', sa.Boolean(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=True),
    sa.Column('destino', sa.String(), nullable=False),
    sa.Column('codigo_uf_destino', sa.Integer(), nullable=False),
    sa.Column('origem', sa.String(), nullable=False),
    sa.Column('codigo_uf_origem', sa.Integer(), nullable=False),
    sa.Column('horario_saida', sa.DateTime(), nullable=True),
    sa.Column('horario_chegada', sa.DateTime(), nullable=True),
    sa.Column('previsao_entrega', sa.DateTime(), nullable=True),
    sa.Column('volume', sa.Float(), nullable=False),
    sa.Column('caminhao_id', sa.Integer(), nullable=True),
    sa.Column('dono_id', sa.Integer(), nullable=False),
    sa.Column('valor_frete', sa.Float(), nullable=False),
    sa.Column('valor_frete_motorista', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['caminhao_id'], ['caminhoes.id'], ),
    sa.ForeignKeyConstraint(['dono_id'], ['usuarios.id'], ),
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
    op.create_table('entregas_realizadas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('carga_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carga_id'], ['cargas.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('carga_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entregas_realizadas')
    op.drop_table('cargas_categorias')
    op.drop_table('cargas')
    op.drop_table('caminhoes')
    op.drop_table('avaliacoes_usuario_motorista')
    op.drop_table('usuarios')
    op.drop_table('municipios')
    op.drop_table('motoristas')
    op.drop_table('estados')
    op.drop_table('categorias')
    # ### end Alembic commands ###