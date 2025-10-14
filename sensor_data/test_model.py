from models import SensorData
from pydantic import ValidationError

valid_data = {
    "sensor_id": "T-1001",
    "temperature_celsius": 25.5,
    "timestamp": "2025-10-08T15:30:00",
}

invalid_data = {
    "sensor_id": "T-1001",
    "temperature_celsius": -51,
    "timestamp": "2025-10-08T15:30:00",
}
validated_reading = SensorData(**valid_data)

print(validated_reading.model_dump())
print(type(validated_reading))
print(validated_reading.sensor_id)

try:
    invalid_reading = SensorData(**invalid_data)
except ValidationError as v:
    for error in v.errors():
        print(error.get("msg"))
