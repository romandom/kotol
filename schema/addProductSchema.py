from pydantic import BaseModel


class AddProduct(BaseModel):
    user_id: str | None = None
    product_id: str | None = None
