from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.dbService import get_db
from schema.addRecipeSchema import AddRecipe

router = APIRouter(
    tags=["Fermentation"],
    responses={404: {"description": "Not found"}},
)


@router.get("/fermentation/get/{recipe_uuid}")
async def get_fermentation(recipe_uuid: str, db: Session = Depends(get_db)):
    return


@router.post("/fermentation/add/{recipe_uuid}")
async def add_fermentation_to_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return


@router.delete("/fermentation/delete/{recipe_uuid}")
async def delete_fermentation_from_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return


@router.put("/fermentation/update/{fermentation_uuid}")
async def update_fermentation(recipe: AddRecipe, db: Session = Depends(get_db)):
    return
