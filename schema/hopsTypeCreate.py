from pydantic import BaseModel


class HopsTypeCreate(BaseModel):
    name: str
    grams: int

    class Config:
        orm_mode = True
