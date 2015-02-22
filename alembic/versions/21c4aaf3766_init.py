"""Init

Revision ID: 21c4aaf3766
Revises: 
Create Date: 2015-02-22 17:03:56.451593

"""

# revision identifiers, used by Alembic.
revision = '21c4aaf3766'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
import pyramidapp


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('group',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', pyramidapp.models.user.MyPassword(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('login')
    )
    op.create_table('right',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_group',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.uid'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.uid'], )
    )
    op.create_table('group_right',
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('right_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.uid'], ),
    sa.ForeignKeyConstraint(['right_id'], ['right.uid'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_right')
    op.drop_table('user_group')
    op.drop_table('right')
    op.drop_table('user')
    op.drop_table('group')
    ### end Alembic commands ###