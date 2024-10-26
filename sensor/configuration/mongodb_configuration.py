import pymongo
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL
import certifi

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name = DATABASE_NAME):

        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            
        except Exception as e:
            raise e