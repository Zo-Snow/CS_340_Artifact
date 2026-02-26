# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, hostname, port, database, collection): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = hostname 
        PORT = port
        DB = database
        COL = collection 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 
        #
        # If the connection is succesful, print "Succesfully Connected"
        print("Succesfully Connected") 
        
    # Method to implement the C in CRUD.    
    def create(self, data):
        if data is not None:
            try:
                # Attempt to insert the document into the collection
                self.database.animals.insert_one(data)
                return True  # Return “True” if insert successful
            except Exception as e:
                # Handle any errors during the insert operation and display error message
                print(f"Error: {e}")
                return False  # Return “False” if insert unsuccessful
        else:
            return False  # Return “False” if insert unsuccessful 

    # Method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            try:
                # Return results as a list if the command is successful
                return list(self.database.animals.find(data))
            except Exception as e:
                # Handle any errors during the read operation and display error message
                print(f"Error: {e}")
                return []  # Return an empty list if the command is unsuccessful
        else:
            return []  # Return an empty list if the command is unsuccessful
        
    # Method to implement the U in CRUD.
    def update(self, data, new_data):
        if data is not None and new_data is not None:
            try:
                # Update matching documents using the provided query and update values
                result = self.database.animals.update_many(data, new_data)
                return result.modified_count  # Return number of modified documents
            except Exception as e:
                # Handle any errors during the update operation and display error message
                print(f"Error: {e}")
                return 0  # Return 0 if update is unsuccessful
        else:
            return 0  # Return 0 if input data is invalid
        
    # Method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            try:
                # Delete matching documents from the collection
                result = self.database.animals.delete_many(data)
                return result.deleted_count  # Return number of deleted documents
            except Exception as e:
                # Handle any errors during the delete operation and display error message
                print(f"Error: {e}")
                return 0  # Return 0 if delete is unsuccessful
        else:
            return 0  # Return 0 if input data is invalid


