from pydantic import BaseModel


class AddProduct(BaseModel):
    user_uuid: str | None = None
    product_uuid: str | None = None
