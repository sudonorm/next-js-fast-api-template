import pandas as pd
import numpy as np
import sys
import os
import sqlalchemy

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if home_dir not in sys.path:
    sys.path.append(home_dir)
if f'{home_dir}{os.sep}{"db"}' not in sys.path:
    sys.path.append(f'{home_dir}{os.sep}{"db"}')
if ".." not in sys.path:
    sys.path.append("..")

from . import dataModel

from glob import glob

from typing import List, Dict, Union, Tuple, Any

import warnings

warnings.filterwarnings("ignore")

### helper funcs
from sqlalchemybulk.helper_functions import HelperFunctions
from sqlalchemybulk.crud_helper_funcs import UploadData, DownloadData, DeleteData

## crud
from sqlalchemybulk.crud import BulkUpload

upload = UploadData(engine=dataModel.engine)


class Upload(HelperFunctions):
    """The Upload class is the core of the upload process. In this class, there are functions which are used to upload data
    to different tables in the database
    """

    def upload_data_with_three_columns(
        self,
        df: pd.DataFrame,
        dbTable: str,
        cols_dict: dict,
        create_pk: bool = True,
        drop_na: bool = True,
        drop_duplicate_entries: bool = False,
    ):
        upload.upload_info(
            df=df,
            dbTable=dbTable,
            cols_dict=cols_dict,
            create_pk=create_pk,
            drop_na=drop_na,
            drop_duplicate_entries=drop_duplicate_entries,
        )

    def upload_data_with_more_than_three_columns(
        self,
        df: pd.DataFrame,
        dbTable: str,
        unique_idx_elements: list,
        column_update_fields: list,
    ):
        upload.upload_info_atomic(
            dbTable=dbTable,
            df=df,
            unique_idx_elements=unique_idx_elements,
            column_update_fields=column_update_fields,
        )

    def upload_user_details_three_cols(
        self,
        df,
        dbTable: str = "dataModel.UserDetail",
        cols_dict: dict = {
            "user_id": "user_id",
        },
        create_pk: bool = True,
        drop_na: bool = True,
        drop_duplicate_entries: bool = False,
    ):

        self.upload_data_with_three_columns(
            df=df,
            dbTable=dbTable,
            cols_dict=cols_dict,
            create_pk=create_pk,
            drop_na=drop_na,
            drop_duplicate_entries=drop_duplicate_entries,
        )

    def upload_any_more_than_three(
        self,
        df: pd.DataFrame,
        dbTable_class: str = "dataModel.UserDetail",
        dbTable_name: str = "user_details",
        pk_key_col: str = "id",
    ):
        dbTable = dataModel.metadata.tables[dbTable_name]
        unique_idx_elements = [
            x
            for x in list(dbTable.constraints)
            if isinstance(x, sqlalchemy.sql.schema.UniqueConstraint)
        ][0]

        unique_idx_elements = [x.name for x in unique_idx_elements]

        all_table_cols = [x.description for x in dbTable.columns._all_columns]

        all_table_cols.remove(pk_key_col)
        column_update_fields = list(set(all_table_cols).difference(unique_idx_elements))

        self.upload_data_with_more_than_three_columns(
            dbTable=dbTable_class,
            df=df,
            unique_idx_elements=unique_idx_elements,
            column_update_fields=column_update_fields,
        )
