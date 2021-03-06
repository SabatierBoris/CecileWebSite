"""Added comment table and relation with Picture

Revision ID: 14de332c829
Revises: 83c8b1f8eb
Create Date: 2015-06-06 19:02:31.166505

"""

# revision identifiers, used by Alembic.
revision = '14de332c829'
down_revision = '83c8b1f8eb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import pyramidapp


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('comment', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('uid')
    )
    op.create_table('item_comment',
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['comment_id'], ['comment.uid'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.uid'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item_comment')
    op.drop_table('comment')
    ### end Alembic commands ###
