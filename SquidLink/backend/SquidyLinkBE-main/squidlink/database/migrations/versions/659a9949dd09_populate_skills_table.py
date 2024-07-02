"""populate skills table

Revision ID: 659a9949dd09
Revises: 25162b263575
Create Date: 2024-07-02 12:00:52.455179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '659a9949dd09'
down_revision: Union[str, None] = '25162b263575'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    skill_names = [
        "Solar Panels",
        "Wind Energy",
        "Efficiency Auditing",
        "Building Design",
        "Waste Materials Management",
        "Environmental Impact Assessment",
        "LEED Certification",
        "HVAC Optimization",
        "Smart Grid Technology",
        "Battery Storage",
        "Energy Policy",
        "Biomass Energy Systems",
        "Hydroelectric Power",
        "Geothermal Systems",
        "Building Management Systems",
        "Water Treatment",
        "Waste Management",
        "Recycling",
        "Landscaping",
        "Electric Vehicle Infrastructure",
    ]

    # Define the table representation
    skills_table = sa.sql.table(
        'skills',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String)
    )

    # Insert skill names
    op.bulk_insert(
        skills_table,
        [{'name': name} for name in skill_names]
    )


def downgrade() -> None:
    pass
