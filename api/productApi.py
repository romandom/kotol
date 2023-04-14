from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.setProductRecipe import SetProductRecipe
from schema.addProductSchema import AddProduct
from schema.setTemparatureSchema import SetTemperatureSchema
from service.dbService import get_db
from service.productService import get_all_products, add_product_to_user, delete, set_online, \
    set_boil, set_actual_temp, get_actual_temp, get_boil_status, finish, get_heat_temperature, stop_boiling

router = APIRouter(
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@router.get("/product/all/{user_id}")
async def get_user_products(user_id: str, db: Session = Depends(get_db)):
    return get_all_products(db, user_id)


@router.post("/product/add")
async def add_product(product: AddProduct, db: Session = Depends(get_db)):
    return add_product_to_user(db, product)


@router.delete("/product/delete/{product_id}")
async def delete_product(product_id: str, db: Session = Depends(get_db)):
    return delete(db, product_id)


@router.post("/product/online/{product_uuid}")
async def set_online_product(product_uuid: str, db: Session = Depends(get_db)):
    return set_online(db, product_uuid)


@router.post("/product/boiling")
async def set_boil_product(set_product_recipe: SetProductRecipe, db: Session = Depends(get_db)):
    return set_boil(db, set_product_recipe)


@router.post("/product/actual_temperature")
async def set_actual_temperature(set_temp: SetTemperatureSchema, db: Session = Depends(get_db)):
    return set_actual_temp(db, set_temp)


@router.get("/product/actual_temperature/{product_id}")
async def get_actual_temperature(product_id: str, db: Session = Depends(get_db)):
    return get_actual_temp(db, product_id)


@router.get("/product/get_boil_status/{product_id}")
async def get_boiling_status(product_id: str, db: Session = Depends(get_db)):
    return get_boil_status(db, product_id)


@router.post("/product/finish/{product_id}")
async def finish_cycle(product_id: str, db: Session = Depends(get_db)):
    return finish(db, product_id)


@router.get("/product/get_heat_temperature/{product_id}")
async def get_heat_info(product_id: str, db: Session = Depends(get_db)):
    return get_heat_temperature(db, product_id)


@router.post("/product/stop_boiling/{product_id}")
async def stop_boiling_process(product_id: str, db: Session = Depends(get_db)):
    return stop_boiling(db, product_id)
