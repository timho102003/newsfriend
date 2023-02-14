from .base_collection import BaseMongoDBCollection


class AuthCollection(BaseMongoDBCollection):
    def get_news_api_key(self, username="timho102003"):
        return str(
            self.collection.find(
                {"username": username}, {"news_api_key": True, "_id": False}
            )[0]["news_api_key"]
        )
