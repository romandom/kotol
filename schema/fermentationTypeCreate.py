from pydantic import BaseModel
from typing import Optional


class FermentationTypeCreate(BaseModel):
    name: str
    amount: int
    grams: bool
    ml: bool

    class Config:
        orm_mode = True
