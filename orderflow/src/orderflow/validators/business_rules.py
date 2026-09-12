"""
Phase 2 — Business Rule Validation

TODO: Cross-field validation logic that can't be expressed by type hints
alone. Examples to implement:

- total == subtotal + tax (within rounding tolerance)
- quantity > 0 for every line item
- no expired promo codes
- currency consistent across all line items

These will mostly live as `@model_validator(mode="after")` methods on the
Order model (or a mixin), plus a few `@field_validator`s for single-field
checks (e.g. quantity > 0).
"""
