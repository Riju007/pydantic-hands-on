# OrderFlow — Roadmap

**Learner profile:** Intermediate-to-advanced Python. Already hands-on with
Pydantic BaseModel, Field, validators, model_config, and computed fields.
Skipping tutorial-level content — this roadmap goes straight into real
production-style patterns.

**Learning mode:** Guided study mode. For each phase: step-by-step
explanation of the concept → short code walkthrough → a question to answer
before moving on. Learner writes code collaboratively (pair-programming
style), not solo and not copy-paste.

**The scenario:** Orders arrive from three sources — a mobile app, a web
store, and a third-party marketplace — each with a different raw schema.
Build a pipeline that validates, normalizes into one unified `Order` model,
and reports data-quality issues instead of crashing.

---

## Phase 0 — Domain Modeling
**Goal:** Design the unified `Order` and `LineItem` models — the clean
target shape everything else normalizes into.

- Decide core fields: identity, customer, line items, money, status, timestamps
- Key lesson: use `Decimal` for money, never `float`
- Files: `src/orderflow/models/line_item.py`, `src/orderflow/models/order.py`
- Concepts: `BaseModel`, `Field`, nested models, `Decimal`, `Literal`, `datetime`

## Phase 1 — Modeling the Messy Sources
**Goal:** Model `MobileOrder`, `WebOrder`, `MarketplaceOrder` — each with
their own field names/shapes — and unify them with a **discriminated union**.

- Each source model has a `source: Literal["mobile"]` (etc.) as a tag
- Combine into `AnyOrderSource = Annotated[Union[...], Field(discriminator="source")]`
- Files: `src/orderflow/models/sources.py`
- Concepts: discriminated unions, `Literal`, `Annotated`, aliasing (`Field(alias=...)`)

## Phase 2 — Business Rule Validation
**Goal:** Enforce rules that span multiple fields — e.g. `total == subtotal + tax`,
no negative quantities, no expired promo codes, currency consistency across line items.

- Files: `src/orderflow/validators/business_rules.py`
- Concepts: `field_validator`, `model_validator(mode="after")`, raising `ValueError`
  inside validators, `ValidationInfo`

## Phase 3 — Normalization
**Goal:** Convert any of the 3 source models into the unified `Order`,
computing derived fields along the way (e.g. total item count, discount %).

- Files: `src/orderflow/normalize.py`
- Concepts: `@computed_field`, `field_serializer`, `model_dump(by_alias=...)`,
  mapping/transform functions

## Phase 4 — Error Handling & Data Quality Reporting
**Goal:** When a record fails validation, don't crash the pipeline — capture
*which* record, *which* field, *why* — and produce a summary report.

- Files: `src/orderflow/errors.py`
- Concepts: catching `pydantic.ValidationError`, `.errors()`, aggregating
  results, designing a `ValidationReport` model

## Phase 5 — Configuration Management
**Goal:** Externalize tunable values (tax rate assumptions, fraud thresholds,
currency) into environment-driven settings instead of hardcoding them.

- Files: `src/orderflow/config.py`, `.env.example`
- Concepts: `pydantic-settings`, `BaseSettings`, `.env` loading, secrets vs config

## Phase 6 — Testing
**Goal:** Build a test suite that proves the pipeline handles both clean
and deliberately broken data correctly.

- Files: `tests/test_models.py`, `tests/fixtures/*.json`
- Concepts: `pytest`, fixture design, testing for expected `ValidationError`s

## Phase 7 — CLI Wrapper (stretch goal)
**Goal:** Make the pipeline runnable from the command line:
`orderflow validate data/sample_input/mobile_orders.json`

- Files: `src/orderflow/cli.py`
- Concepts: `typer` (or `argparse`), wiring the pipeline end-to-end

---

## Suggested order of attack
0 → 1 → 2 → 3 → 4 → 5 → 6 → (7 optional, anytime after 6)

Phases 0–3 are the conceptual core of the project (this is "real Pydantic").
Phases 4–6 are what separates a toy script from something portfolio-worthy.
