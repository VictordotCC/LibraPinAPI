"""empty message

Revision ID: 8822cba6b77b
Revises: 
Create Date: 2022-10-23 20:34:29.785720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8822cba6b77b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=28), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('imagen', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imagen', sa.String(length=250), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('contenido', sa.String(length=250), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pin_board',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pin_id', sa.Integer(), nullable=False),
    sa.Column('board_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.ForeignKeyConstraint(['pin_id'], ['pin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pin_categoria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pin_id', sa.Integer(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categoria.id'], ),
    sa.ForeignKeyConstraint(['pin_id'], ['pin.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pin_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pin_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pin_id'], ['pin.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pin_tag')
    op.drop_table('pin_categoria')
    op.drop_table('pin_board')
    op.drop_table('pin')
    op.drop_table('usuario')
    op.drop_table('tag')
    op.drop_table('categoria')
    op.drop_table('board')
    # ### end Alembic commands ###