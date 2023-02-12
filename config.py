import os
import pandas as pd

# TODO: Conneect to Dataset Country List
COUNTRY_LIST = [("United States", "#"), ("Canada", "#")]

TEST_IMG_ROOT = (
    "./assets/imgs" 
)

TEST_NEWS = pd.read_csv("test_dataset/test_dataset.csv")

def concat_path(imgname):
    return os.path.join(TEST_IMG_ROOT, imgname)


TEST_NEWS["imgname"] = TEST_NEWS["imgname"].apply(concat_path)

MAINPAGE_ARTICLE_CARD_CONFIG = {"row_style": "p-2"}

__all__ = [COUNTRY_LIST, TEST_NEWS, MAINPAGE_ARTICLE_CARD_CONFIG]
