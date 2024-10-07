from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    ConfigDict,
    create_model,
    SecretStr,
)
from typing import Annotated, Optional, Union
from pydantic.json_schema import SkipJsonSchema
import datetime

# Define the annotated type with constraints
ConstrainedStr = Annotated[
    Optional[str], Field(strip_whitespace=True, min_length=1, max_length=50)
]
PasswordStr = Annotated[SecretStr, Field(strip_whitespace=True, min_length=8)]


class UserBase(BaseModel):
    email: EmailStr
    first_name: ConstrainedStr = None
    last_name: ConstrainedStr = None


class UserCreate(UserBase):
    password: PasswordStr
    model_config = {"extra": "forbid"}


class UserToken(
    create_model(
        "UserCreate",
        **{"email": (ConstrainedStr, ...), "password": (ConstrainedStr, ...)}
    )  ### only include the email and password fields
):
    model_config = {"extra": "forbid"}


class UserCheck(
    create_model(
        "UserCreate", **{"email": (ConstrainedStr, ...)}
    )  ### only include the email and password fields
):
    model_config = {"extra": "forbid"}


class UserOut(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True


class UserInDB(UserOut):
    hashed_password: str


class UserDetails(BaseModel):
    address: str
    phone_number: str


class UserDetailsEdited(UserDetails):
    message: str


class UserItems(BaseModel):
    id: int
    name: str
    description: str
    price: float
    slugs: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
