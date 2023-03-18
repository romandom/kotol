from pydantic import BaseModel


class AddRecipe(BaseModel):
    user: str | None = None
    name: str | None = None
    beer_type: str | None = None
    degrees: str | None = None
    style: str | None = None
    date: str | None = None
    shared: bool | None = None
    date: str | None = None
    ibu: str | None = None
    color: str | None = None
    alcohol: str | None = None
    decoction: bool | None = None
    infusion: bool | None = None
    info: str | None = None
    note: str | None = None
