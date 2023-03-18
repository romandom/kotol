from pydantic import BaseModel


class RegisterUser(BaseModel):
    username: str | None = None
    password: str | None = None


class UserInDB(RegisterUser):
    hashed_password: str
