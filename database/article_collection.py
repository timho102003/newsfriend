from .base_collection import BaseMongoDBCollection


class ArticleCollection(BaseMongoDBCollection):
    def __init__(
        self, ip_address, port=27018, database_name="newsfriend", collection_name=None
    ):
        super().__init__(ip_address, port, database_name, collection_name)

    def retrieve_article(self, lang=None, _id=None):
        projection = {"dateTimePub":True, "title":True, "body": True, "authors": True, "image": True, "_id": True, "url": True}
        if lang is not None and _id is not None:
            query = {"lang": lang, "_id": _id}
            func = "find"
            return list(getattr(self.collection, func)(query, projection))
        elif lang is not None:
            query = {"lang": lang}
            func = "find"
            return list(getattr(self.collection, func)(query, projection))
        elif _id is not None:
            query = {"_id": _id}
            func = "find_one"
            return dict(getattr(self.collection, func)(query, projection))
        else:
            raise Exception
        return list(getattr(self.collection, func)(query, projection))