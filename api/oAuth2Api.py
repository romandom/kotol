from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schema.userSchema import User, UserInDB
from schema.registerSchema import RegisterUser
from service.dbService import get_db
from service.oAuth2Service import authenticate_user, create_access_token, get_current_user, \
    ACCESS_TOKEN_EXPIRE_MINUTES, register_user

router = APIRouter(
    tags=["Auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer", "user_id": user.id}


@router.post("/register")
async def register(user: RegisterUser, db: Session = Depends(get_db)):
    return await register_user(user, db)


@router.get("/users/me/")
async def read_users_me(user: UserInDB = Depends(get_current_user)):
    return {"user": user}


