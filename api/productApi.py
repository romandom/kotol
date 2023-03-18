from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.addProductSchema import AddProduct
from service.dbService import get_db
from service.productService import get_all_products, add_product_to_user, delete

router = APIRouter(
    tags=["Product"],
    responses={404: {"description": "Not found"}},
)


@router.get("/product/all/{user_uuid}")
async def get_user_products(user_uuid: str, db: Session = Depends(get_db)):
    return get_all_products(db, user_uuid)


@router.post("/product/add")
async def add_product(product: AddProduct, db: Session = Depends(get_db), ):
    return add_product_to_user(db, product)


@router.delete("/product/delete/{product_uuid}")
async def delete_product(product_uuid: str, db: Session = Depends(get_db)):
    return delete(db, product_uuid)
