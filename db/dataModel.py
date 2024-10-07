from __future__ import annotations

import inspect as sys_inspect
from sqlalchemy import create_engine, event, inspect, Index, UniqueConstraint, MetaData
from sqlalchemy.orm import declarative_base, registry, relationship, sessionmaker
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
    MetaData,
    Boolean,
    BigInteger,
    DateTime,
    Date,
    Numeric,
    Text,
    Float,
    DATETIME,
)

from dataclasses import dataclass, field
from typing import List, Optional, Union
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import types
from sqlalchemy.dialects.mysql.base import MSBinary
import uuid
import subprocess

import os
import json
import re
import shutil
from pathlib import Path
import builtins
import sys
import datetime

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if home_dir not in sys.path:
    sys.path.append(home_dir)

from sqlalchemybulk.manager import Migrate, Connection
from sqlalchemybulk.helper_functions import HelperFunctions

from sys import platform as pltfrm_type

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

CREATE_MIGRATION_FILE = True
RUN_MIGRATION = True
DROP_ALEMBIC_TABLE_AND_STAMP_HEAD = False
IS_SQLITE = True
ENABLE_MIGRATION = True

SLSH = os.sep

BASEPATH = home_dir

helper_funcs = HelperFunctions()
con = Connection()

mapper_registry = registry()
Base = mapper_registry.generate_base()

db_uri = os.getenv("DB_URI")
alembic_path = os.getenv("ALEMBIC_PATH", home_dir)

script_location = f'{alembic_path}{os.sep}{"alembic"}'

if IS_SQLITE:
    db_uri = os.getenv("SQLITE_DB_PATH")
    sqlite_file_path = db_uri
    sqlite_file = db_uri
    db_uri = f"sqlite:///{sqlite_file}"

else:
    sqlite_file_path = ""

engine = create_engine(db_uri, echo=False)
metadata = MetaData()
metadata.reflect(bind=engine)

##################################

SessionLocal = sessionmaker(bind=engine)

### Tables


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)

    user_details = relationship("UserDetail", back_populates="user")

    __table_args__ = (
        UniqueConstraint(email, name="u_email_usr"),
        Index("idx_email_usr", "email", unique=True, postgres_using="gin"),
    )


class UserDetail(Base):
    __tablename__ = "user_details"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_usrid_ud"))
    address = Column(Text)
    phone_number = Column(Text)

    user = relationship("User", back_populates="user_details")

    __table_args__ = (
        UniqueConstraint(user_id, name="u_usrid_ud"),
        Index("idx_user_id_e", "user_id", unique=False, postgres_using="btree"),
    )


class UserItem(Base):
    __tablename__ = "user_items"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", name="fk_usrid_ui"))
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    slugs = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint(user_id, slugs, name="u_usrid_slg_ui"),
        Index("idx_user_id_ui", "user_id", unique=False, postgres_using="btree"),
    )


####### DO NOT DELETE ######

if ENABLE_MIGRATION:
    migrate = Migrate(
        script_location=script_location,
        uri=db_uri,
        is_sqlite=IS_SQLITE,
        db_file_path=sqlite_file_path,
        create_migration_file=CREATE_MIGRATION_FILE,
        run_migration=RUN_MIGRATION,
        drop_alembic_stamp_head=DROP_ALEMBIC_TABLE_AND_STAMP_HEAD,
    )
    if migrate.check_for_migrations():
        migrate.init_db()
