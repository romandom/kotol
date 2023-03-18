from pydantic import BaseModel
from typing import List


class MashSchema(BaseModel):
    time: str | None = None
    type: str | None = None
    amount: str | None = None
    info: str | None = None
    note: str | None = None


class MashList(BaseModel):
    data: List[MashSchema]
