from base_collection import BaseMongoDBCollection


class ArticleCollection(BaseMongoDBCollection):
    def __init__(
        self, ip_address, port=27018, database_name="newsfriend", collection_name=None
    ):
        super().__init__(ip_address, port, database_name, collection_name)
