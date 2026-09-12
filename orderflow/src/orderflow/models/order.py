"""
Phase 0 — Domain Modeling

TODO: Define the unified Order model — the clean target shape that all
three messy source schemas (Phase 1) will eventually normalize into.

Think about: identity, customer, nested line items, money (subtotal/tax/
total), status, and timestamps.
"""

from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel

from orderflow.models.line_item import LineItem


class Order(BaseModel):
    # TODO: order_id: str
    # TODO: source: Literal["mobile", "web", "marketplace"]
    # TODO: customer_email: str
    # TODO: items: list[LineItem]
    # TODO: subtotal: Decimal
    # TODO: tax: Decimal
    # TODO: total: Decimal
    # TODO: status: str
    # TODO: placed_at: datetime
    pass
