import pymongo


class Database(object):
    # class var
    URI = None
    DATABASE = None

    @staticmethod
    def initialize(URI, collection):
        client = pymongo.MongoClient(URI)
        Database.DATABASE = client.get_default_database() 
    
    # Add one data
    @staticmethod
    def insert_one(collection, data): # data is a dict
        Database.DATABASE[collection].insert_one(data)

    # Add a list of data
    @staticmethod
    def insert_many(collection, data): # data is a list of dict
        Database.DATABASE[collection].insert_many(data)
        
    # Find one data with search tokens
    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)       

    # Find a list of data with search tokens
    @staticmethod
    def find(collection, query):
        return [job for job in Database.DATABASE[collection].find(query)]
    
    # Update one data
    @staticmethod
    def update_one(collection, query, update):
        return Database.DATABASE[collection].update_one(query, update)
    
    # Update a list of data
    @staticmethod
    def update_many(collection, query, update):
        return Database.DATABASE[collection].update_many(query, update)
    
    # Delete a list of data matching search tokens
    @staticmethod
    def delete_many(collection, query):
        Database.DATABASE[collection].delete_many(query)   
    
