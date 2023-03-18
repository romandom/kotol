import http
import uuid

from sqlalchemy.orm import Session
from schema.maltSchema import MaltSchema, MaltList

import models


def get(db: Session, recipe_uuid: str):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_uuid).first().malt


def add(db: Session, recipe_uuid: str, malt: MaltList):
    for x in malt.data:
        db_mash = models.Malt(id=uuid.uuid4(), time=x.time,
                              type=x.type, amount=x.amount, degrees=x.degrees, info=x.info, note=x.note, recipe_id=recipe_uuid)
        db.add(db_mash)
    db.commit()
    return http.HTTPStatus.OK


def delete(db: Session, recipe_uuid: str):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_uuid).first()
    for malt in db_recipe.malt:
        db.query(models.Mash).filter(models.Malt.id == malt.id).delete()
    db.commit()
    return http.HTTPStatus.OK


def update(db: Session, malt_uuid: str, malt: MaltSchema):
    if not malt_uuid:
        return "Missing uuid"
    if malt.info != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.info: malt.info})
    if malt.type != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.type: malt.type})
    if malt.note != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.note: malt.note})
    if malt.amount != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.amount: malt.amount})
    if malt.time != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.time: malt.time})
    if malt.degrees != "":
        db.query(models.Malt).filter(models.Malt.id == malt_uuid).update({models.Malt.degrees: malt.degrees})
    db.commit()
    return http.HTTPStatus.OK
