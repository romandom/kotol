from pydantic import BaseModel


class User(BaseModel):
    id: str
    email: str | None = None
    date: str | None = None
    is_active: bool | None = None


class UserInDB(User):
    hashed_password: str
