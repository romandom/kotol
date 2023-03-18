from pydantic import BaseModel
from typing import List


class MaltSchema(BaseModel):
    time: str | None = None
    degrees: str | None = None
    type: str | None = None
    amount: str | None = None
    info: str | None = None
    note: str | None = None


class MaltList(BaseModel):
    data: List[MaltSchema]
