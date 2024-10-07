import pandas as pd
import numpy as np
import sys
import os

home_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if home_dir not in sys.path:
    sys.path.append(home_dir)
if f'{home_dir}{os.sep}{"db"}' not in sys.path:
    sys.path.append(f'{home_dir}{os.sep}{"db"}')
if ".." not in sys.path:
    sys.path.append("..")

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

    # FILE: str = r"/path/to/some_data.json"

    # some_data: pd.DataFrame = pd.read_json(FILE)

    # upload.upload_some_data(df=some_data)

    test_items = [
        {
            "user_id": 1,
            "name": "Headphones",
            "description": "This can be used to listen to soul lifting music",
            "price": 99,
            "slugs": "asdf4324/headphones",
        },
        {
            "user_id": 1,
            "name": "iPhone",
            "description": "Access the world from your pocket",
            "price": 599,
            "slugs": "asdf4324/iphone",
        },
        {
            "user_id": 1,
            "name": "Batman Costume",
            "description": "Great gear for important work",
            "price": 79,
            "slugs": "asdf4324/batman-costume",
        },
        {
            "user_id": 2,
            "name": "Headphones",
            "description": "This can be used to listen to soul lifting music",
            "price": 99,
            "slugs": "asdf4324/headphones",
        },
        {
            "user_id": 2,
            "name": "iPhone",
            "description": "Access the world from your pocket",
            "price": 599,
            "slugs": "asdf4324/iphone",
        },
        {
            "user_id": 2,
            "name": "Batman Costume",
            "description": "Great gear for important work",
            "price": 79,
            "slugs": "asdf4324/batman-costume",
        },
        {
            "user_id": 3,
            "name": "Headphones",
            "description": "This can be used to listen to soul lifting music",
            "price": 99,
            "slugs": "asdf4324/headphones",
        },
        {
            "user_id": 3,
            "name": "iPhone",
            "description": "Access the world from your pocket",
            "price": 599,
            "slugs": "asdf4324/iphone",
        },
        {
            "user_id": 3,
            "name": "Batman Costume",
            "description": "Great gear for important work",
            "price": 79,
            "slugs": "asdf4324/batman-costume",
        },
        {
            "user_id": 4,
            "name": "Headphones",
            "description": "This can be used to listen to soul lifting music",
            "price": 99,
            "slugs": "asdf4324/headphones",
        },
        {
            "user_id": 4,
            "name": "iPhone",
            "description": "Access the world from your pocket",
            "price": 599,
            "slugs": "asdf4324/iphone",
        },
        {
            "user_id": 4,
            "name": "Batman Costume",
            "description": "Great gear for important work",
            "price": 79,
            "slugs": "asdf4324/batman-costume",
        },
    ]

    items = pd.DataFrame(test_items)

    upload.upload_any_more_than_three(
        df=items,
        dbTable_class="dataModel.UserItem",
        dbTable_name="user_items",
        pk_key_col="id",
    )

    #########################################################################################

    print("All uploads are done")


if __name__ == "__main__":
    main()
