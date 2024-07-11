from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

class MongoDBHelper:
    #Driver Code upto print(e)
    def __init__(self,collection="users"):
        uri = "mongodb+srv://radhika:radhika9@cluster0.ku8ndcy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        
        #Only if you face SSL error
        ca = certifi.where()

        #Create a new Client and connect to the server
        #client = MongoClient(uri,server_api= ServerApi('1'))
        #Only if you face SSL error , add ->tlsCAFile = ca
        client = MongoClient(uri, tlsCAFile=ca, server_api= ServerApi('1'))

        #Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your Deployement.You successfully Connected to MongoDb!")
        
        except Exception as e:
            print(e)

        #Get reference to the Database
        self.db = client['Python']
        self.collection = self.db[collection]

    #insert_one = function, document = dictionary
    def insert(self,document):
        result= self.collection.insert_one(document)
        print("Document inserted in Collection: ",self.collection.name)
        #print("Result is:",result,result._inserted_id)
        print("result is: ",result)
        return result

    #select * from Database
    #query as input will act as condition, what to delete,what to fetch, what to update
    def fetch(self, query =""):
        documents = self.collection.find(query)
        return list(documents)
    
    def delete(self, query =""):
        result = self.collection.delete_one(query)
        print("result is: ",result)
        return result

    def update(self,document,query):
        document_to_update = {'$set': document}
        result = self.collection.update_one(query,document_to_update)
        print("result is: ",result)
        return result
