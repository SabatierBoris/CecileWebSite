"""Correct comment system

Revision ID: 21e136af704
Revises: 14de332c829
Create Date: 2015-06-23 19:27:52.254302

"""

# revision identifiers, used by Alembic.
revision = '21e136af704'
down_revision = '14de332c829'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import pyramidapp


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_comment')
    op.add_column('comment', sa.Column('item_id', sa.Integer(), nullable=True))
    op.add_column('comment', sa.Column('parent_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comment', 'item', ['item_id'], ['uid'])
    op.create_foreign_key(None, 'comment', 'comment', ['parent_id'], ['uid'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_constraint(None, 'comment', type_='foreignkey')
    op.drop_column('comment', 'parent_id')
    op.drop_column('comment', 'item_id')
    op.create_table('item_comment',
    sa.Column('comment_id', sa.INTEGER(), nullable=True),
    sa.Column('item_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.uid'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.uid'], )
    )
    ### end Alembic commands ###
