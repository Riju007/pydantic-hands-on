"""
Phase 5 — Configuration Management

TODO: Externalize tunable values using pydantic-settings' BaseSettings,
loaded from a .env file (see .env.example at the project root).

Things that belong here rather than being hardcoded:
- default currency
- tax rate assumptions (if used for cross-checks)
- fraud / anomaly thresholds (e.g. max reasonable order total)
"""

# from pydantic_settings import BaseSettings
#
# class Settings(BaseSettings):
#     default_currency: str = "USD"
#     max_reasonable_order_total: int = 10_000
#
#     class Config:
#         env_file = ".env"
