import pandas as pd
import numpy as np
import sys
import os

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append("..")
sys.path.append(home_dir)
sys.path.append(f'{home_dir}{os.sep}{"db"}')

from glob import glob
import re
from typing import List, Dict, Union, Tuple

import warnings

warnings.filterwarnings("ignore")

### helper funcs
from sqlalchemybulk.helper_functions import HelperFunctions
from sqlalchemybulk.crud_helper_funcs import UploadData, DownloadData, DeleteData

## crud
from sqlalchemy import select

from db.upload_data import Upload
from db.delete_data import Delete
from db.download_data import Download

import json

upload = Upload()
download = Download()
delete = Delete()


from dotenv import load_dotenv

load_dotenv()


def main():
    ##### CHANGE THE PATHS!!!
    ################### For first time setup of static datasets, read in the datasets and upload ############################

    FILE: str = r"/path/to/some_data.json"

    some_data: pd.DataFrame = pd.read_json(FILE)

    upload.upload_some_data(df=some_data)

    #########################################################################################

    print("All uploads are done")


if __name__ == "__main__":
    main()
