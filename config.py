import os

import pandas as pd

# TODO: Conneect to Dataset Country List
COUNTRY_LIST = [("United States", "#"), ("Canada", "#")]

TEST_IMG_ROOT = (
    "./assets/imgs"
)
TEST_NEWS = pd.read_csv("test_dataset/test_article.csv")


def concat_path(imgname):
    return os.path.join(TEST_IMG_ROOT, imgname)


TEST_NEWS["imgname"] = TEST_NEWS["imgname"].apply(concat_path)

MAINPAGE_ARTICLE_CARD_CONFIG = {"margin": 10}

## Google Adsense:

adsense_code = '''
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6648185162891118"
     crossorigin="anonymous"></script>
<!-- NewsFriend -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-6648185162891118"
     data-ad-slot="5890224535"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
'''
__all__ = [COUNTRY_LIST, TEST_NEWS, MAINPAGE_ARTICLE_CARD_CONFIG, adsense_code]
