# OrderFlow

A multi-source e-commerce order validation & normalization engine, built with Pydantic v2.

Ingests messy order data from three fictional sources (mobile app, web store,
marketplace API), validates it, normalizes it into one clean unified schema,
and reports on records that fail validation — the way a real data-quality
pipeline would.

See `roadmap.md` for the full build plan (phase by phase).

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Project layout

See the tree below (also described in `roadmap.md`).

```
orderflow/
├── src/orderflow/
│   ├── models/
│   │   ├── line_item.py      # LineItem model (Phase 0)
│   │   ├── order.py          # Unified Order model (Phase 0)
│   │   └── sources.py        # MobileOrder / WebOrder / MarketplaceOrder (Phase 1)
│   ├── validators/
│   │   └── business_rules.py # Cross-field validation logic (Phase 2)
│   ├── normalize.py          # source model -> unified Order (Phase 3)
│   ├── errors.py             # Error aggregation & reporting (Phase 4)
│   ├── config.py             # pydantic-settings config (Phase 5)
│   └── cli.py                # Optional CLI entrypoint (Phase 7, stretch)
├── tests/
│   ├── fixtures/              # Sample JSON data per source, incl. broken records
│   └── test_models.py
├── data/sample_input/         # Raw sample files to feed the pipeline
├── requirements.txt
└── roadmap.md
```
