import http

from sqlalchemy.orm import Session

import models


def set_boiling(db: Session, product_uuid):
    product = db.query(models.Product).filter(models.Product.id == product_uuid).first()
    if product.boiled:
        db.query(models.Product).filter(models.Product.id == product_uuid).update({models.Product.boiled: False})
        db.commit()
        return {
            "Code": http.HTTPStatus.OK,
            "Message": "Boiled set to false"
        }
    db.query(models.Product).filter(models.Product.id == product_uuid).update({models.Product.boiled: True})
    db.commit()
    return {
        "Code": http.HTTPStatus.OK,
        "Message": "Boiled set to true"
    }


def get_temperature():
    return None