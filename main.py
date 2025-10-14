from fastapi import FastAPI

from sensor_data.models import SensorData

app = FastAPI(debug=True)


@app.post("/sensors/")
def record_sensor_data(data: SensorData):
    """Receives and validate sensors data based on the Pydantic model."""
    result = {"message": "Data successfully received and validate", "data": data}
    return result
