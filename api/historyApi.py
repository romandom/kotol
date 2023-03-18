from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.dbService import get_db
from service.recipeService import list_of_recipes, get_recipe as get_one, add_recipe as add
from schema.addRecipeSchema import AddRecipe

router = APIRouter(
    tags=["History"],
    responses={404: {"description": "Not found"}},
)


@router.get("/history/all/{user_uuid}")
async def get_history_list(user_uuid: str, db: Session = Depends(get_db)):
    return list_of_recipes(db, user_uuid)


@router.post("/history/add")
async def add_to_history(db: Session = Depends(get_db)):
    return


@router.delete("/history/delete/{history_uuid}")
async def delete_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    return add(db, recipe)
