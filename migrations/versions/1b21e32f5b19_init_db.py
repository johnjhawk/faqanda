"""init db

Revision ID: 1b21e32f5b19
Revises: 
Create Date: 2018-02-21 05:48:04.983167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b21e32f5b19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('tag_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=240), nullable=True),
    sa.Column('last_visited', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('question',
    sa.Column('q_id', sa.Integer(), nullable=False),
    sa.Column('q_title', sa.String(length=140), nullable=True),
    sa.Column('q_date', sa.DateTime(), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.CLOB(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('q_id')
    )
    op.create_index(op.f('ix_question_q_date'), 'question', ['q_date'], unique=False)
    op.create_table('question_comment',
    sa.Column('qc_id', sa.Integer(), nullable=False),
    sa.Column('q_id', sa.Integer(), nullable=True),
    sa.Column('qc_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('deleted', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['q_id'], ['question.q_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('qc_id')
    )
    op.create_index(op.f('ix_question_comment_qc_date'), 'question_comment', ['qc_date'], unique=False)
    op.create_table('question_tag',
    sa.Column('q_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['q_id'], ['question.q_id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.tag_id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('question_tag')
    op.drop_index(op.f('ix_question_comment_qc_date'), table_name='question_comment')
    op.drop_table('question_comment')
    op.drop_index(op.f('ix_question_q_date'), table_name='question')
    op.drop_table('question')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('tag')
    # ### end Alembic commands ###
