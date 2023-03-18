from pydantic import BaseModel


class ListSchema(BaseModel):
    recipe_uuid: str | None = None
    recipe_name: str | None = None
