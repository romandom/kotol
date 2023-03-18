from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.dbService import get_db
from service.recipeService import list_of_recipes, get_recipe as get_one, add_recipe as add
from schema.addRecipeSchema import AddRecipe

router = APIRouter(
    tags=["Recipe"],
    responses={404: {"description": "Not found"}},
)


@router.get("/recipe/all/{user_uuid}")
async def get_recipes_list(user_uuid: str, db: Session = Depends(get_db)):
    return list_of_recipes(db, user_uuid)


@router.get("/recipe/get/{recipe_uuid}")
async def get_recipe(recipe_uuid: str, db: Session = Depends(get_db)):
    return get_one(db, recipe_uuid)


@router.post("/recipe/add")
async def add_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    return add(db, recipe)


@router.delete("/recipe/delete/{recipe_uuid}")
async def delete_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    return add(db, recipe)


@router.put("/recipe/update/{recipe_uuid}")
async def update_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    return add(db, recipe)
