import os

import pandas as pd

# TODO: Conneect to Dataset Country List
COUNTRY_LIST = [("United States", "#"), ("Canada", "#")]

TEST_IMG_ROOT = (
    "./assets/imgs"  # "/Users/timho102003/Documents/newsfriend/test_dataset/imgs"
)
TEST_NEWS = pd.read_csv("test_dataset/test_article.csv")


def concat_path(imgname):
    return os.path.join(TEST_IMG_ROOT, imgname)


TEST_NEWS["imgname"] = TEST_NEWS["imgname"].apply(concat_path)

__all__ = [COUNTRY_LIST, TEST_NEWS]
