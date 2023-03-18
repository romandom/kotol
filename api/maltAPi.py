from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema.maltSchema import MaltList, MaltSchema

from service.dbService import get_db
from service.maltService import get, add, delete, update

router = APIRouter(
    tags=["Malt"],
    responses={404: {"description": "Not found"}},
)


@router.get("/malt/get/{recipe_uuid}")
async def get_mash(recipe_uuid: str, db: Session = Depends(get_db)):
    return get(db, recipe_uuid)


@router.post("/malt/add/{recipe_uuid}")
async def add_mash_to_recipe(recipe_uuid: str, malt: MaltList, db: Session = Depends(get_db)):
    return add(db, recipe_uuid, malt)


@router.delete("/malt/delete/{recipe_uuid}")
async def delete_mash_from_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return delete(db, recipe_uuid)


@router.put("/malt/update/{malt_uuid}")
async def update_mash(malt: MaltSchema, mash_uuid: str, db: Session = Depends(get_db)):
    return update(db, mash_uuid, malt)
