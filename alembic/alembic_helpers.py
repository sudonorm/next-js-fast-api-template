from alembic import op
from sqlalchemy import engine_from_config
from sqlalchemy.engine import reflection
from sqlalchemy import create_engine

import os
import sys

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if home_dir not in sys.path:
    sys.path.append(home_dir)

from db.dataModel import db_uri


def table_does_not_exist(table, schema=None):
    engine = create_engine(db_uri, echo=False)
    insp = reflection.Inspector.from_engine(engine)
    return insp.has_table(table, schema) == False


def table_has_column(table, column):
    engine = create_engine(db_uri, echo=False)
    insp = reflection.Inspector.from_engine(engine)
    has_column = False
    for col in insp.get_columns(table):
        if column not in col["name"]:
            continue
        has_column = True
    return has_column
