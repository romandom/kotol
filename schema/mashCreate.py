from pydantic import BaseModel
from typing import Optional


class MashCreate(BaseModel):
    time: str
    type: str
    amount: str
    info: str
    note: str

    class Config:
        orm_mode = True
