from pydantic import BaseModel
from enums import temperatureEnum


class GetTemperature(BaseModel):
    product_uuid: str | None = None
    type: temperatureEnum.TypeOfBoiling | None = None
