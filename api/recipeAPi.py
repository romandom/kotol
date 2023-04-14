from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from service.dbService import get_db
from service.recipeService import list_of_author_recipes, get_recipe as get_one, add_recipe as add, delete, \
    list_of_all_recipes
from schema.addRecipeSchema import AddRecipe
from schema.recipeCreate import RecipeCreate
import models

router = APIRouter(
    tags=["Recipe"],
    responses={404: {"description": "Not found"}},
)


@router.get("/recipe/all/{user_id}")
async def get_recipes_of_author_list(user_id: str, db: Session = Depends(get_db)):
    return list_of_author_recipes(db, user_id)


@router.get("/recipe/all")
async def get_recipes_list(db: Session = Depends(get_db)):
    return list_of_all_recipes(db)


@router.get("/recipe/get/{recipe_id}")
async def get_recipe(recipe_id: str, db: Session = Depends(get_db)):
    return get_one(db, recipe_id)


@router.post("/recipe/add")
async def add_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    return add(db, recipe)


@router.delete("/recipe/delete/{recipe_id}")
async def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return delete(db, recipe_id)


@router.put("/recipe/update/{recipe_uuid}")
async def update_recipe(recipe: AddRecipe, db: Session = Depends(get_db)):
    return add(db, recipe)
