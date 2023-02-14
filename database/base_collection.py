import pymongo

class BaseMongoDBCollection:
    def __init__(self, ip_address, port=27018, database_name="newsfriend", collection_name=None):
        '''
        https://pymongo.readthedocs.io
        '''
        self.port = port
        self.ip_address = ip_address
        self.database_name = database_name
        self.collection_name = collection_name

        self.__client = pymongo.MongoClient(self.ip_address, self.port)
        self.__db = self.__client[self.database_name]
        self.__collection = self.__db[self.collection_name]

    @property
    def collection(self):
        return self.__collection