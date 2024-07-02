"""Creates all tables

Revision ID: 25162b263575
Revises:
Create Date: 2024-07-01 16:08:45.998651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25162b263575'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'facilities',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('address_line_1', sa.String, nullable=True),
        sa.Column('address_line_2', sa.String, nullable=True),
        sa.Column('address_postcode', sa.String, nullable=True),
        sa.Column('address_city', sa.String, nullable=True),
        sa.Column('address_country', sa.String, nullable=True),
        sa.Column('bms', sa.String, nullable=True),
        sa.Column('sector', sa.Enum('AGRICULTURE', 'COMMERCIAL', 'INDUSTRIAL', 'RESIDENTIAL', 'OTHER', name='facilitysector'), nullable=False),
        sa.Column('floor_area_square_metres', sa.Integer, nullable=True),
    )

    op.create_table(
        'meter_readings',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('facility_id', sa.Integer, sa.ForeignKey('facilities.id', ondelete='CASCADE'), nullable=False),
        sa.Column('data_source', sa.Enum('OCTOPUS_API', name='meterreadingdatasource'), nullable=False),
        sa.Column('type', sa.Enum('ELECTRICITY', 'GAS', name='meterreadingtype'), nullable=False),
        sa.Column('consumption', sa.Float, nullable=False),
        sa.Column('unit', sa.Enum('KWH', name='meterreadingunit'), nullable=False),
        sa.Column('interval_start', sa.DateTime, nullable=False),
        sa.Column('interval_end', sa.DateTime, nullable=False),
    )

    op.create_table(
        'projects',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('facility_id', sa.Integer(), sa.ForeignKey('facilities.id', ondelete='CASCADE'), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
    )

    op.create_table(
        'contractors',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address_line_1', sa.String(), nullable=True),
        sa.Column('address_line_2', sa.String(), nullable=True),
        sa.Column('address_postcode', sa.String(), nullable=True),
        sa.Column('address_city', sa.String(), nullable=True),
        sa.Column('address_country', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'skills',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table(
        'contractors_skills',
        sa.Column('contractor_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['contractor_id'], ['contractors.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('contractor_id', 'skill_id')
    )

    op.create_table(
        'projects_skills',
        sa.Column('project_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
        sa.ForeignKeyConstraint(['skill_id'], ['skills.id'], ),
        sa.PrimaryKeyConstraint('project_id', 'skill_id')
    )

    op.create_table(
        'bids',
        sa.Column('id', sa.Integer(), primary_key=True, nullable=False),
        sa.Column('contractor_id', sa.Integer, sa.ForeignKey('contractors.id', ondelete='CASCADE'), nullable=False),
        sa.Column('project_id', sa.Integer, sa.ForeignKey('projects.id', ondelete='CASCADE'), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('duration', sa.Integer(), nullable=False),
        sa.Column('site_inspection', sa.Boolean(), nullable=False),
        sa.Column('estimated_savings', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('bids')
    op.drop_table('projects_skills')
    op.drop_table('contractors_skills')
    op.drop_table('skills')
    op.drop_table('contractors')
    op.drop_table('projects')
    op.drop_table('meter_readings')
    op.drop_table('facilities')
