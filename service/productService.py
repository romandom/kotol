import http

from sqlalchemy.orm import Session

import models
from schema.addProductSchema import AddProduct
from schema.setProductRecipe import SetProductRecipe
from schema.setTemparatureSchema import SetTemperatureSchema


def get_all_products(db: Session, user_id):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "User not exists"
        }
    products = []
    for product in user.products:
        products.append({'id': product.id, 'name': product.name, 'online': product.online})
    return products


def add_product_to_user(db: Session, add_product: AddProduct):
    db_product = db.query(models.Product).filter(models.Product.id == add_product.product_id).first()
    if db_product.user_id is not None:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "Product is already assigned to user"
        }
    db.query(models.Product).filter(models.Product.id == add_product.product_id).update(
        {models.Product.user_id: add_product.user_id})
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Product assigned to user"
    }


def delete(db: Session, product_uuid):
    db.query(models.Product).filter(models.Product.id == product_uuid).update({models.Product.user_id: None})
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Product removed"
    }


def set_online(db: Session, product_uuid):
    product = db.query(models.Product).filter(models.Product.id == product_uuid).first()
    if product.online:
        db.query(models.Product).filter(models.Product.id == product_uuid).update({models.Product.online: False})
        db.commit()
        return {
            "Code": http.HTTPStatus.OK,
            "Message": "Online set to false"
        }
    db.query(models.Product).filter(models.Product.id == product_uuid).update({models.Product.online: True})
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Online set to true"
    }


def set_boil(db: Session, set_product_recipe: SetProductRecipe):
    product = db.query(models.Product).filter(models.Product.id == set_product_recipe.product_id).first()
    if product.boiled:
        return {
            "IN_USE"
        }
    if product.online is not True:
        return {
            "NOT_ONLINE"
        }
    db_recipe = db.query(models.Recipe).filter(models.Recipe.id == set_product_recipe.recipe_id).first()
    db.query(models.Product).filter(models.Product.id == set_product_recipe.product_id).update(
        {models.Product.boiled: True, models.Product.actual_recipe: db_recipe.name})
    for malt in db_recipe.malt:
        db.add(models.Boling(product_id=set_product_recipe.product_id, temperature=malt.degrees, time=malt.time))
    db.add(models.Boling(product_id=set_product_recipe.product_id, temperature='100', time='90'))
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Boiled set to true"
    }


def get_actual_temp(db: Session, product_id: str):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if db_product.boiled is False:
        return {
            "actual": 0,
            "requested": 0
        }
    return {
        'actual': db_product.temperature,
        'requested': db_product.temperatures[0].temperature
    }


def set_actual_temp(db: Session, obj: SetTemperatureSchema):
    db.query(models.Product).filter(models.Product.id == obj.product_id).update(
        {models.Product.temperature: obj.temperature})
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Temperature was saved"
    }


def get_boil_status(db: Session, product_id: str):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if len(db_product.temperatures) == 1:
        fase = 'Sladovar'
    elif len(db_product.temperatures) == 1:
        fase = 'Chmelovar'
    if db_product.boiled is False:
        return {
            "recipe": '',
            "fase": ''
        }
    return {
        "recipe": db_product.actual_recipe,
        "fase": fase
    }


def finish(db: Session, product_id: str):
    db_product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if len(db_product.temperatures) == 0:
        return "Finished"
    for temp in db_product.temperatures:
        if(len(db_product.temperatures) == 1):
            db_product.temperature = 0
            db_product.boiled = False
            db_product.actual_recipe = ''
        db_product.temperatures.remove(temp)
        db.delete(temp)
        break
    db.commit()
    return "OK"


def get_heat_temperature(db: Session, product_id: str):
    db_recipe = db.query(models.Product).filter(models.Product.id == product_id).first()
    for temp in db_recipe.temperatures:
        return {
            "temperature": temp.temperature,
            "time": temp.time
        }
    return "not ok"


def stop_boiling(db: Session, product_id: str):
    db.query(models.Product).filter(models.Product.id == product_id).update({models.Product.boiled: False})
    db.commit()
    return "OK"


# def check_uuid(uuid: UUID):
#     try:
#         UUID(uuid)
#     except ValueError:
#         return False
#     return True
