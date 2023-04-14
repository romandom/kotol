from pydantic import BaseModel


class SetProductRecipe(BaseModel):
    product_id: str
    recipe_id: str
