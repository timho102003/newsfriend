from datetime import date, timedelta

import requests
import yaml

from database import ArticleCollection, AuthCollection

db_cfg = yaml.safe_load(open("./database/db_cfg.yaml"))

auth_db = AuthCollection(
    ip_address=db_cfg["mongodb"]["ip_address"],
    database_name=db_cfg["mongodb"]["database_name"],
    collection_name=db_cfg["mongodb"]["auth_collection_name"],
    port=db_cfg["mongodb"]["port"],
)

news_api_db = ArticleCollection(
    ip_address=db_cfg["mongodb"]["ip_address"],
    database_name=db_cfg["mongodb"]["database_name"],
    collection_name=db_cfg["mongodb"]["news_collection_name"],
)

if db_cfg["news_api"]["dateStart"] == -1 or db_cfg["news_api"]["dateEnd"] == -1:
    yesterday = date.today() - timedelta(days=1)
    the_day_before_yesterday = date.today() - timedelta(days=2)
    db_cfg["news_api"]["dateStart"] = the_day_before_yesterday.strftime("%Y-%m-%d")
    db_cfg["news_api"]["dateEnd"] = yesterday.strftime("%Y-%m-%d")

for lang in db_cfg["news_api"]["language"]:
    endpoint = db_cfg["news_api"]["getArticleEndpoint"]
    params = {
        "apiKey": auth_db.get_news_api_key(username=db_cfg["news_api"]["api_key_name"]),
        "articlesPage": db_cfg["news_api"]["articlesPage"],
        "articlesCount": db_cfg["news_api"]["articlesCount"],
        "articlesSortBy": db_cfg["news_api"]["articlesSortBy"],
        "articlesSortByAsc": False,
        "articlesArticleBodyLen": db_cfg["news_api"]["articlesArticleBodyLen"],
        "resultType": db_cfg["news_api"]["resultType"],
        "dataType": db_cfg["news_api"]["dataType"],
        "dateStart": db_cfg["news_api"]["dateStart"],
        "dateEnd": db_cfg["news_api"]["dateEnd"],
        "lang": lang,
    }
    # Send the API request
    response = requests.get(endpoint, params=params)

    # Check the response status code
    if response.status_code == 200:
        data = response.json()
        data = data["articles"]["results"]
        news_api_db.collection.insert_many(data)
    else:
        print("Request failed with status code:", response.status_code)
