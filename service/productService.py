import http

from sqlalchemy.orm import Session
from uuid import UUID

import models
from schema.addProductSchema import AddProduct


def get_all_products(db: Session, user_uuid):
    if check_uuid(user_uuid) is False:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "UUID of user is not valid"
        }
    user = db.query(models.User).filter(models.User.id == user_uuid).first()
    if user is None:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "User not exists"
        }
    products = []
    for product in user.products:
        products.append(product.id)
    return products


def add_product_to_user(db: Session, add_product: AddProduct):
    if check_uuid(add_product.user_uuid) is False:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "UUID of user is not valid"
        }
    if check_uuid(add_product.product_uuid) is False:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "UUID of product is not valid"
        }
    if db.query(models.Product).filter(models.Product.id == add_product.product_uuid).first() is not None:
        return {
            "Code": http.HTTPStatus.BAD_REQUEST,
            "Message": "Product is already assigned to user"
        }
    product = models.Product(id=add_product.product_uuid, user_id=add_product.user_uuid)
    db.add(product)
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Product assigned to user"
    }


def delete(db: Session, product_uuid):
    db.query(models.Product).filter(models.Product.id == product_uuid).delete()
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Product removed"
    }


def check_uuid(uuid: UUID):
    try:
        UUID(uuid)
    except ValueError:
        return False
    return True
