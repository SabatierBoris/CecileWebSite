"""Add validating comment

Revision ID: 2b10b84cbc7
Revises: 21e136af704
Create Date: 2015-07-05 09:03:41.658173

"""

# revision identifiers, used by Alembic.
revision = '2b10b84cbc7'
down_revision = '21e136af704'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import pyramidapp


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('fk_category_item', 'category', 'item', ['uid'], ['uid'])
    op.add_column('comment', sa.Column('valid', sa.Boolean(), nullable=False))
    op.alter_column('comment', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comment', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('comment', 'valid')
    op.drop_constraint('fk_category_item', 'category', type_='foreignkey')
    ### end Alembic commands ###