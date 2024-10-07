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

from db.schemas import UserItems
from db.dataModel import User, UserDetail, SessionLocal, engine
from db.download_data import Download
from .users import get_current_active_user, get_current_active_superuser, get_db

download = Download()

router = APIRouter()


def get_items(
    user_id: int,
) -> dict:

    user_items = download.get_unlimited_data_from(
        table="user_items",
        add_clause=True,
        clause_col="user_id",
        clause_col_values=[user_id],
        orient="records",
    )

    if len(user_items) > 0:
        user_items = user_items
    else:
        user_items = False

    if user_items:
        return user_items  # [UserItems(**user_item) for user_item in user_items]
    else:
        return False


@router.get(
    "", include_in_schema=False
)  ### exception added to guide agianst the 307 redirect error on cloud servers
@router.get(
    "/",
    # response_model=List[UserItems],
    status_code=status.HTTP_200_OK,
)
async def get_user_items(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db),
) -> ORJSONResponse:

    items = get_items(user_id=current_user.id)

    if not items:
        raise HTTPException(
            status_code=404,
            detail="Either the user does not exist or no items were found.",
        )
    else:
        return ORJSONResponse(content=items, status_code=200)
