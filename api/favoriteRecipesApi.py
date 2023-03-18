from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.dbService import get_db

router = APIRouter(
    tags=["Favorites"],
    responses={404: {"description": "Not found"}},
)


@router.get("/favorites/all")
async def get_favorites(db: Session = Depends(get_db)):
    return


@router.post("/favorites/add/{recipe_uuid}")
async def add_recipe_to_favorites(recipe_uuid: str, db: Session = Depends(get_db)):
    return


@router.delete("/favorites/delete/{recipe_uuid}")
async def delete_favorite_from_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return
