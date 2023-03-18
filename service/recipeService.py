import uuid
import http

from sqlalchemy.orm import Session
from datetime import datetime

import models
from schema import recipesListSchema, addRecipeSchema


def list_of_recipes(db: Session, user_uuid):
    user_db = db.query(models.User).filter(models.User.id == user_uuid).first()
    recipes_list = []
    for recipe in user_db.recipes:
        recipes_list.append(recipesListSchema.ListSchema(recipe_uuid=str(recipe.id), recipe_name=recipe.name))
    return recipes_list


def get_recipe(db: Session, recipe_uuid):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_uuid).first()


def add_recipe(db: Session, recipe: addRecipeSchema.AddRecipe):
    if recipe.user is None:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "User uuid is empty"
        }
    if recipe.decoction and recipe.infusion or not recipe.decoction and not recipe.infusion:
        return {
            "Code": http.HTTPStatus.CONFLICT,
            "Message": "Decoction and infusion cannot be both true or false"
        }
    if db.query(models.User).filter(models.User.id == recipe.user).first() is None:
        return {
            "Code": http.HTTPStatus.CONFLICT,
            "Message": "User does not exists"
        }
    db.add(models.Recipe(id=uuid.uuid4(), name=recipe.name, beer_type=recipe.beer_type,
                         degrees=recipe.degrees, style=recipe.style, date=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                         shared=recipe.shared, ibu=recipe.ibu, color=recipe.color, alcohol=recipe.alcohol,
                         decoction=recipe.decoction, infusion=recipe.infusion, info=recipe.info, note=recipe.note,
                         user_id=recipe.user))
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Recipe added"
    }

