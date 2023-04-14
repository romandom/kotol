from pydantic import BaseModel


class MaltCreate(BaseModel):
    time: str
    degrees: int
    info: str
    note: str

    class Config:
        orm_mode = True
