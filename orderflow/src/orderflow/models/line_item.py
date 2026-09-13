"""
Phase 0 — Domain Modeling

TODO: Define the LineItem model.

A LineItem represents a single product within an order: what was bought,
how many, and at what price. Remember: money should be Decimal, not float.
"""

from uuid import uuid4
from typing import Literal
from decimal import Decimal
from datetime import datetime, timezone

from pydantic import BaseModel, UUID4, Field, PositiveInt


class LineItem(BaseModel):
    # TODO: sku: str
    # TODO: quantity: int
    # TODO: unit_price: Decimal
    # pass
    product_id: UUID4 = Field(
        default_factory=uuid4, description="Unique id of the product"
    )
    name: str = Field(..., description="Name of the product")
    price: Decimal = Field(
        ..., gt=0, decimal_places=2, description="Price of the product"
    )
    quantity: PositiveInt = Field(default=1, lt=1000, description="Quantity Purchased")
    currency: Literal["USD", "EUR", "GBP", "INR"] = Field(
        default="USD", description="Used currency"
    )
    category: str | None = Field(
        description="category of the product", repr=False, default=None
    )


ORDER_STATUS = Literal[
    "pending",
    "delivered",
    "returned",
    "cancelled",
    "shipped",
    "out_for_delivery",
]

PAYMENT_STATUS = Literal[
    "paid",
    "cash_on_delivery",
    "refund",
]


class Order(BaseModel):
    """Order model"""

    order_id: UUID4 = Field(default_factory=uuid4, description="Unique order id")
    customer_name: str = Field(
        ..., max_length=100, description="Full name of the customer"
    )
    line_items: list[LineItem] = Field(
        default_factory=list, description="Items in the order"
    )
    status: ORDER_STATUS = Field(default="pending", description="Order status")
    payment_status: PAYMENT_STATUS = Field(..., description="Status of the payment")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Order created at",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Order updated at",
    )
