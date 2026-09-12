"""
Phase 0 — Domain Modeling

TODO: Define the LineItem model.

A LineItem represents a single product within an order: what was bought,
how many, and at what price. Remember: money should be Decimal, not float.
"""

from decimal import Decimal

from pydantic import BaseModel


class LineItem(BaseModel):
    # TODO: sku: str
    # TODO: quantity: int
    # TODO: unit_price: Decimal
    pass
