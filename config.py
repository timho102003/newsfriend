import os

import numpy as np
import pandas as pd

# TODO: Conneect to Dataset Country List
COUNTRY_LIST = [
    ("us", "eng", "America/Los_Angeles"),
    ("korea", "kor", "Asia/Seoul"),
    ("japan", "jpn", "Asia/Tokyo"),
    ("france", "fra", "Europe/Paris"),
    ("taiwan&china", "zho", "Asia/Taipei"),
]

# TEST_IMG_ROOT = "./assets/imgs"

# TEST_NEWS = pd.read_csv("test_dataset/test_dataset.csv")
# TEST_NEWS = TEST_NEWS.replace(np.nan, None)


# def concat_path(imgname):
#     return os.path.join(TEST_IMG_ROOT, imgname)

# TEST_NEWS["imgname"] = TEST_NEWS["imgname"].apply(concat_path)

TIMEZONE = "America/Los_Angeles"
# COUNTRY_LANG_TABLE = {
#     "us": "eng",
#     "france": "fra",
#     "china&taiwan": "zho",
#     "japan": "jpn",
#     "korea": "kor"
# }

MAINPAGE_ARTICLE_CARD_CONFIG = {"row_style": "p-2"}
NO_IMG_URL = "./assets/imgs/no_img_url.png"

__all__ = [COUNTRY_LIST, MAINPAGE_ARTICLE_CARD_CONFIG]
