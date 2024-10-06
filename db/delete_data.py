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
from sqlalchemy import func, select, update, and_, delete, insert

## crud
from sqlalchemybulk.crud import BulkUpload

delete_ = DeleteData(engine=dataModel.engine)


class Delete(HelperFunctions):

    def delete_user_details(self, batch: list) -> None:

        query = delete(dataModel.UserDetail).where(
            dataModel.UserDetail.user_id.in_(batch)
        )
        delete_.delete_data_on_condition(
            dbTable="dataModel.UserDetail", statement=query
        )
