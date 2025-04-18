#First- MongoDB File to verify it's Set-up
"""
    MongoDB CRUD Operations
    1. Install the Pymongo Library
        pip install "pymongo[srv]"
    2. Iff you face any error for SSL
        pip install certifi     
"""

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi

uri = "mongodb+srv://radhika:<password>@cluster0.ku8ndcy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

ca = certifi.where()
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile = ca,server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

#Get reference to the database
db = client['Python']

#Get Collection Names from Database
collections = db.list_collection_names()

for collection in collections:
    print(collection)

#To view Data present inside Documents

documents = db['users'].find()
print(documents)

for document in documents:
    print(document)
