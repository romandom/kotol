from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.mashSchema import MashList, MashSchema

from service.dbService import get_db
from service.mashService import get, add, delete, update

router = APIRouter(
    tags=["Mash"],
    responses={404: {"description": "Not found"}},
)


@router.get("/mash/get/{recipe_uuid}")
async def get_mash(recipe_uuid: str, db: Session = Depends(get_db)):
    return get(db, recipe_uuid)


@router.post("/mash/add/{recipe_uuid}")
async def add_mash_to_recipe(recipe_uuid: str, mash: MashList, db: Session = Depends(get_db)):
    return add(db, recipe_uuid, mash)


@router.delete("/mash/delete/{recipe_uuid}")
async def delete_mash_from_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return delete(db, recipe_uuid)


@router.put("/mash/update/{mash_uuid}")
async def update_mash(mash: MashSchema, mash_uuid: str, db: Session = Depends(get_db)):
    return update(db, mash_uuid, mash)
