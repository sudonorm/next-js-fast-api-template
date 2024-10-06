from fastapi import APIRouter, Depends, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse, ORJSONResponse

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from sqlalchemy.orm import Session
from sqlalchemy import select

import pandas as pd
import numpy as np
import json
import time
import re

from typing import Annotated, Any, Union, List, Optional, Dict, Tuple, Generator

from app.core.config import settings
from app.core import security

from random import choice

from db.schemas import (
    UserCreate,
    UserOut,
    Token,
    UserInDB,
    TokenData,
    UserToken,
    UserCheck,
    UserDetails,
    UserDetailsEdited,
)
from db.dataModel import User, UserDetail, SessionLocal, engine
from db.download_data import Download

download = Download()

router = APIRouter()


# Dependency
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(
    email: str,
) -> UserInDB:

    user_exists = download.get_unlimited_data_from(
        table="users",
        add_clause=True,
        clause_col="email",
        clause_col_values=[email],
        orient="records",
    )

    if len(user_exists) > 0:
        user_exists = user_exists[0]
    else:
        user_exists = False

    if user_exists:
        return UserInDB(**user_exists)
    else:
        return False


def authenticate_user(email: str, password: str) -> UserOut:
    user = get_user(email=email)
    if not user:
        return False
    if not security.verify_password(password, user.hashed_password):
        return False
    return user


@router.post(
    "", include_in_schema=False
)  ### exception added to guide agianst the 307 redirect error on cloud servers
@router.post(
    "/",
    response_model=UserOut,
    response_model_exclude=["password"],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
) -> Response:

    if not security.is_password_strong(str(user.password.get_secret_value())):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.",
        )
    user_exists = db.query(User).filter(User.email == user.email).first()
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered."
        )
    hashed_password = security.get_password_hash(user.password.get_secret_value())
    new_user = User(
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post(
    "/check",
    response_model=UserOut,
    response_model_exclude=["password", "hashed_password"],
)
async def check_user_in_db(
    token: Annotated[str, Depends(security.JWTBearer())],
    user: UserCheck,
    db: Session = Depends(get_db),
) -> UserInDB:

    user = get_user(email=user.email)

    if not user:
        raise HTTPException(status_code=404, detail="User does not exist.")
    return user


async def get_current_user(
    token: Annotated[str, Depends(security.JWTBearer())]
) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.decodeJWT(token=token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except:
        raise credentials_exception
    user = get_user(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[UserOut, Depends(get_current_user)],
) -> UserInDB:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_active_superuser(
    current_user: User = Depends(get_current_user),
) -> UserInDB:
    if not current_user.is_superuser:
        raise HTTPException(status_code=400, detail="Not enough privileges.")
    return current_user


@router.post("/token", response_model=Token)
def login_for_access_token(
    # form_data: UserToken = Depends(), ## form format
    form_data: UserToken,  ## JSON format
) -> Token:
    user = authenticate_user(email=form_data.email, password=form_data.password)

    if not user or not security.verify_password(
        form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(subject=user.email)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
async def read_users_me(
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
) -> UserOut:
    return current_user


@router.post("/me/edit_user_details", response_model=UserDetailsEdited)
async def edit_users_me(
    current_user: Annotated[UserOut, Depends(get_current_active_user)],
    # user_details: UserDetails = Depends(),
    user_details: UserDetails,
    db: Session = Depends(get_db),
) -> UserDetailsEdited:
    message = f"Phewww your details were edited, {current_user.first_name} :)"

    user_details_edit = UserDetail(
        user_id=current_user.id,
        address=user_details.address,
        phone_number=user_details.phone_number,
    )
    db.add(user_details_edit)
    db.commit()
    db.refresh(user_details_edit)

    return {
        "message": message,
        "address": user_details_edit.address,
        "phone_number": user_details_edit.phone_number,
    }
