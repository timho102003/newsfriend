import yaml

from database import ArticleCollection

mongodb_cfg = yaml.safe_load(open("./database/db_cfg.yaml"))["mongodb"]
article_database = ArticleCollection(
    ip_address=mongodb_cfg["ip_address"],
    database_name=mongodb_cfg["database_name"],
    collection_name=mongodb_cfg["news_collection_name"],
    port=mongodb_cfg["port"],
)

# __all__ = ["article_database"]
