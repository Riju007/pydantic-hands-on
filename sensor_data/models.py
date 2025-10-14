from datetime import datetime
from pydantic import BaseModel, Field


class SensorData(BaseModel):
    """Model for sensor data."""

    sensor_id: str
    temperature_celsius: float = Field(
        ...,
        ge=-50.00,
        le=150.00,
        examples=[-20, 50, 100],
        description="Temperature of the sensor",
    )
    timestamp: datetime
