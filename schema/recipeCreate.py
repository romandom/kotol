from pydantic import BaseModel, validator
from schema.maltCreate import MaltCreate
from schema.mashCreate import MashCreate
from schema.fermentationCreate import FermentationCreate
from schema.hopsTypeCreate import HopsTypeCreate
from schema.mashTypeCreate import MashTypeCreate
from schema.fermentationTypeCreate import FermentationTypeCreate
from typing import Optional


class RecipeCreate(BaseModel):
    name: str
    tag: str
    beer_type: str
    degrees: str
    style: str
    shared: bool
    date: str
    ibu: str
    color: str
    alcohol: str
    decoction: bool
    infusion: bool
    info: str
    note: str
    mladina: str
    user_id: int
    malt: list[MaltCreate]
    mash: list[MashCreate]
    fermentation: list[FermentationCreate]
    start_water: str
    splash_water: str
    mash_type: list[MashTypeCreate]
    hops_type: list[HopsTypeCreate]
    fermentation_type: list[FermentationTypeCreate]

    @validator('user_id')
    def validate_user_id(cls, v):
        if v <= 0:
            raise ValueError('user_id must be greater than 0')
        return v

    class Config:
        orm_mode = True
