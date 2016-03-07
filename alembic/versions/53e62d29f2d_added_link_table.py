"""Added link table

Revision ID: 53e62d29f2d
Revises: 2b10b84cbc7
Create Date: 2016-03-06 20:43:32.040776

"""

# revision identifiers, used by Alembic.
revision = '53e62d29f2d'
down_revision = '2b10b84cbc7'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import pyramidapp


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('link',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['item.uid'], ),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('link')
    ### end Alembic commands ###
