"""
Phase 6 — Testing

TODO: Test the pipeline against both clean and deliberately broken fixture
data (see tests/fixtures/). Cover:

- Each source model parses valid raw data correctly
- Invalid data (bad types, negative quantities, mismatched totals) raises
  pydantic.ValidationError
- normalize() produces a correct unified Order for each source
- The error-reporting layer (Phase 4) correctly aggregates multiple bad records
"""

import pytest


def test_placeholder():
    # TODO: replace with real tests once Phase 0-1 models exist
    assert True
