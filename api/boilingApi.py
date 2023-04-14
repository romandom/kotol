from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.getTemperatureSchema import GetTemperature

from service.dbService import get_db

from service.boilingService import set_boiling, get_temperature

router = APIRouter(
    tags=["Boiling"],
    responses={404: {"description": "Not found"}},
)


@router.post("/set_boiling/{product_uuid}")
async def set_boiling_product(product_uuid: str, db: Session = Depends(get_db)):
    return set_boiling(db, product_uuid)


@router.post("/get_temperatures/{product_uuid}")
async def get_temperatures(get_temperature: GetTemperature, db: Session = Depends(get_db)):
    return get_temperature(db, get_temperature)
