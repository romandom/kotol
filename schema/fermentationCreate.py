from pydantic import BaseModel
from typing import Optional


class FermentationCreate(BaseModel):
    time: str
    degrees: int
    info: str
    note: str

    class Config:
        orm_mode = True
