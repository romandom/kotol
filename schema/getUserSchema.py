from pydantic import BaseModel


class getUser(BaseModel):
    username: str | None = None
    id: str | None = None


class UserInDB(getUser):
    hashed_password: str
