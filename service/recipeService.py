import http

from sqlalchemy.orm import Session, joinedload, subqueryload
from datetime import datetime

import models
from schema import recipesListSchema
from schema.recipeCreate import RecipeCreate


def list_of_author_recipes(db: Session, user_id):
    user_db = db.query(models.User).filter(models.User.id == user_id).first()
    recipes_list = []
    for recipe in user_db.recipes:
        recipes_list.append(
            recipesListSchema.ListSchema(recipe_uuid=str(recipe.id), recipe_name=recipe.name, author=user_db.username,
                                         tag=recipe.tag, alcohol=recipe.alcohol, ibu=recipe.ibu))
    return recipes_list


def list_of_all_recipes(db: Session):
    recipes_db = db.query(models.Recipe).filter(models.Recipe.shared == True).all()
    recipes_list = []
    for recipe in recipes_db:
        recipes_list.append(
            recipesListSchema.ListSchema(recipe_uuid=str(recipe.id), recipe_name=recipe.name,
                                         author=recipe.user.username,
                                         tag=recipe.tag, alcohol=recipe.alcohol, ibu=recipe.ibu))
    return recipes_list


def get_recipe(db: Session, recipe_id):
    return db.query(models.Recipe).options(
        joinedload("malt"),
        joinedload("mash"),
        joinedload("fermentation"),
        joinedload("fermentation_type"),
        joinedload("hops_type"),
        joinedload("mash_type")
    ).filter(models.Recipe.id == recipe_id).first()


def add_recipe(db: Session, recipe: RecipeCreate):
    if db.query(models.User).filter(models.User.id == recipe.user_id).first() is None:
        return {
            "Code": http.HTTPStatus.CONFLICT,
            "Message": "User does not exists"
        }
    db_recipe = models.Recipe(name=recipe.name, tag=recipe.tag, beer_type=recipe.beer_type, degrees=recipe.degrees,
                              style=recipe.style, shared=recipe.shared, date=datetime.now(), ibu=recipe.ibu,
                              color=recipe.color, alcohol=recipe.alcohol, decoction=recipe.decoction,
                              mladina=recipe.mladina,
                              infusion=recipe.infusion,
                              info=recipe.info, note=recipe.note, user_id=recipe.user_id,
                              splash_water=recipe.splash_water, start_water=recipe.start_water)
    if recipe.malt is not None:
        for malt in recipe.malt:
            db_malt = models.Malt(time=malt.time, degrees=malt.degrees,
                                  info=malt.info,
                                  note=malt.note)
            db_recipe.malt.append(db_malt)
    if recipe.mash is not None:
        for mash in recipe.mash:
            db_mash = models.Mash(time=mash.time, type=mash.type, amount=mash.amount, info=mash.info, note=mash.note)
            db_recipe.mash.append(db_mash)
    if recipe.fermentation is not None:
        for fermentation in recipe.fermentation:
            db_fermentation = models.Fermentation(time=fermentation.time, degrees=fermentation.degrees,
                                                  info=fermentation.info, note=fermentation.note)
            db_recipe.fermentation.append(db_fermentation)
    if recipe.mash_type is not None:
        for mash_type in recipe.mash_type:
            db_mash_type = models.MashType(name=mash_type.name, kilograms=mash_type.kilograms)
            db_recipe.mash_type.append(db_mash_type)
    if recipe.hops_type is not None:
        for hops in recipe.hops_type:
            db_hops_type = models.HopsType(name=hops.name, grams=hops.grams)
            db_recipe.hops_type.append(db_hops_type)
    if recipe.fermentation_type is not None:
        for fermentation_type in recipe.fermentation_type:
            db_fermentation_type = models.FermentationType(name=fermentation_type.name, amount=fermentation_type.amount,
                                                           grams=fermentation_type.grams, ml=fermentation_type.ml)
            db_recipe.fermentation_type.append(db_fermentation_type)
    db.add(db_recipe)
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Recipe added"
    }


def delete(db: Session, recipe_id: int):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    for mash in db_recipe.mash:
        db.delete(mash)
    for malt in db_recipe.malt:
        db.delete(malt)
    for fermentation in db_recipe.fermentation:
        db.delete(fermentation)
    for mash_type in db_recipe.mash_type:
        db.delete(mash_type)
    for hops_type in db_recipe.hops_type:
        db.delete(hops_type)
    for fermentation_type in db_recipe.fermentation_type:
        db.delete(fermentation_type)
    db.delete(db_recipe)
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Recipe deleted"
    }
