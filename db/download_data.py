import pandas as pd
import numpy as np
import sys
import os

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append("..")
sys.path.append(home_dir)
sys.path.append(f'{home_dir}{os.sep}{"db"}')

from . import dataModel

from glob import glob

from typing import List, Dict, Union, Tuple, Any

import warnings

warnings.filterwarnings("ignore")

### helper funcs
from sqlalchemybulk.helper_functions import HelperFunctions
from sqlalchemybulk.crud_helper_funcs import UploadData, DownloadData, DeleteData
from sqlalchemy import select, and_

## crud
from sqlalchemybulk.crud import BulkUpload

download_data = DownloadData(engine=dataModel.engine)


class Download(HelperFunctions):
    """The Download class is the core of the query process. In this class, there are functions which are used to download data
    from different tables in the database using a query statement
    """

    def get_unlimited_data_from(
        self,
        table: str,
        add_clause: bool = False,
        clause_col: str = None,
        clause_col_values: list | dict = None,
        orient: bool = False,
    ) -> Union[pd.DataFrame, dict]:
        """Query all the data data in a table in the DB

        Args:
            table (str): Defaults to categories_level

        Returns:
            pd.DataFrame: dataframe containing the data from the table
        """

        query = False

        if table == "user_details":
            if add_clause:
                query = select(
                    dataModel.UserDetail,
                ).where(
                    eval(f'{"dataModel.UserDetail."}{clause_col}').in_(
                        clause_col_values
                    )
                )
            else:
                query = select(
                    dataModel.UserDetail,
                )

        if query:
            df = download_data.download_info_using_session(statement=query)

            if orient:
                df_dict = df.to_dict(orient=orient)
                return df_dict

            return df
        else:
            return pd.DataFrame()
