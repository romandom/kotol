from pydantic import BaseModel


class MashTypeCreate(BaseModel):
    name: str
    kilograms: str

    class Config:
        orm_mode = True
