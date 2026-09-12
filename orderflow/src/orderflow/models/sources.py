"""
Phase 1 — Modeling the Messy Sources

TODO: Define MobileOrder, WebOrder, and MarketplaceOrder — each reflecting
the (different!) raw shape that source actually sends. Then combine them
into a discriminated union, e.g.:

    AnyOrderSource = Annotated[
        Union[MobileOrder, WebOrder, MarketplaceOrder],
        Field(discriminator="source"),
    ]

Each model needs a `source: Literal[...]` field acting as the discriminator
tag. Field names/aliases will likely differ per source (e.g. web might send
"total_price", marketplace might send "order_total").
"""

from typing import Literal, Union

from pydantic import BaseModel, Field
from typing_extensions import Annotated


class MobileOrder(BaseModel):
    source: Literal["mobile"]
    # TODO: remaining mobile-specific fields


class WebOrder(BaseModel):
    source: Literal["web"]
    # TODO: remaining web-specific fields


class MarketplaceOrder(BaseModel):
    source: Literal["marketplace"]
    # TODO: remaining marketplace-specific fields


# TODO: AnyOrderSource = Annotated[Union[MobileOrder, WebOrder, MarketplaceOrder], Field(discriminator="source")]
