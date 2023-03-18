import http
import uuid

from sqlalchemy.orm import Session
from schema.mashSchema import MashSchema, MashList

import models


def get(db: Session, recipe_uuid: str):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_uuid).first().mash


def add(db: Session, recipe_uuid: str, mash: MashList):
    for x in mash.data:
        db_mash = models.Mash(id=uuid.uuid4(), time=x.time,
                              type=x.type, amount=x.amount, info=x.info, note=x.note, recipe_id=recipe_uuid)
        db.add(db_mash)
    db.commit()
    return http.HTTPStatus.OK


def delete(db: Session, recipe_uuid: str):
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_uuid).first()
    for mash in db_recipe.mash:
        db.query(models.Mash).filter(models.Mash.id == mash.id).delete()
    db.commit()
    return http.HTTPStatus.OK


def update(db: Session, mash_uuid: str, mash: MashSchema):
    if not mash_uuid:
        return "Missing uuid"
    if mash.time != "":
        db.query(models.Mash).filter(models.Mash.id == mash_uuid).update({models.Mash.time: mash.time})
    if mash.info != "":
        db.query(models.Mash).filter(models.Mash.id == mash_uuid).update({models.Mash.info: mash.info})
    if mash.type != "":
        db.query(models.Mash).filter(models.Mash.id == mash_uuid).update({models.Mash.type: mash.type})
    if mash.note != "":
        db.query(models.Mash).filter(models.Mash.id == mash_uuid).update({models.Mash.note: mash.note})
    if mash.amount != "":
        db.query(models.Mash).filter(models.Mash.id == mash_uuid).update({models.Mash.amount: mash.amount})
    db.commit()
    return http.HTTPStatus.OK
