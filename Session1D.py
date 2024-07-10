from Session1C import MongoDBHelper
from Session1A import User
from bson.objectid import ObjectId #Import ObjectId, if we widh to fetch document based on Hashcode
import datetime
from tabulate import tabulate

def main():

    print("Welcome to MongoDB Test App")
    dbHelper = MongoDBHelper()

    """
    user = User()
    user.add_user_details()
    document = vars(user)
    dbHelper.insert(document)
    """
    #Fetching your Result
    #query = {"email":"ram123@gmail.com"}

    #query ={"_id": ObjectId("668b8d70bd7c42ef52949f75")}
    
    #For Deleting a Query
    #dbHelper.delete(query)

    #Updating any Query
    query = {"email":"sita@example.com"}
    document_data_to_update ={ "name":"Sita kumari","age":30,"created_on":datetime.datetime.now()}
   # dbHelper.update(document= document_data_to_update,query=query)

    users = dbHelper.fetch()
    #users = dbHelper.fetch(query)
    #columns = ["_id","name","phone","email","password",age","gender","created_on"]
   # headers = users[0].key()
    print(tabulate(users, tablefmt ='grid'))
    #for user in users:
     #  print(user)
    

if __name__ == "__main__":
    main()



