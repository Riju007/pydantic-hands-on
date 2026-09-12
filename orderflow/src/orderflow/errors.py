"""
Phase 4 — Error Handling & Data Quality Reporting

TODO: When a raw record fails validation, capture *which* record, *which*
field(s), and *why* — instead of letting the pipeline crash. Aggregate
these into a report you could hand to a data-quality dashboard.

Consider designing:

    class RecordError(BaseModel):
        record_index: int
        field: str
        message: str

    class ValidationReport(BaseModel):
        total_records: int
        valid_count: int
        invalid_count: int
        errors: list[RecordError]

Populate this by catching pydantic.ValidationError and walking its
.errors() output.
"""
