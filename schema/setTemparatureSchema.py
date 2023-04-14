from pydantic import BaseModel


class SetTemperatureSchema(BaseModel):
    product_id: str
    temperature: str
