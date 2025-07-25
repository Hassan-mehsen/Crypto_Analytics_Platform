"""v3: add FK crypto_id -> dim_crypto_id in fact_exchange_assets

Revision ID: 243445aead18
Revises: 4a4bafa7b8b7
Create Date: 2025-05-20 00:10:45.495633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '243445aead18'
down_revision: Union[str, None] = '4a4bafa7b8b7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'fact_exchange_assets', 'dim_crypto_id', ['crypto_id'], ['crypto_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'fact_exchange_assets', type_='foreignkey')
    # ### end Alembic commands ###
