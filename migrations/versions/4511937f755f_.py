"""empty message

Revision ID: 4511937f755f
Revises: 4d17e120c24a
Create Date: 2025-05-25 12:05:51.579241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4511937f755f'
down_revision = '4d17e120c24a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_table',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id_planet'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'planet_id')
    )
    with op.batch_alter_table('peoples', schema=None) as batch_op:
        batch_op.alter_column('vehicle_people',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('planet_vehicle',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.alter_column('planet_vehicle',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('peoples', schema=None) as batch_op:
        batch_op.alter_column('vehicle_people',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.drop_table('user_table')
    # ### end Alembic commands ###
