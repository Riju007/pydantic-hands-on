"""
Phase 3 — Normalization

TODO: Functions that convert any of the three source models
(MobileOrder / WebOrder / MarketplaceOrder) into the unified Order model.

Also a good place to introduce @computed_field — e.g. a derived
`item_count` or `discount_percent` on Order that isn't in the raw input
but is useful in the normalized output.
"""

from orderflow.models.order import Order

# from orderflow.models.sources import AnyOrderSource


def normalize(raw_order) -> Order:
    """TODO: dispatch on raw_order.source and map fields into an Order."""
    raise NotImplementedError
