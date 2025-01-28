""" Flask

1. pip install Flask

Framework - It is the set of tools used to create other web applications
"""
#Software As A Service Project

from flask import *
import datetime
import hashlib
from database1 import MongoDBHelper
from bson.objectid import ObjectId

#Create the Object of Flask -> It represents 

web_app = Flask("Levi's Exclusive Store ")
db_helper = MongoDBHelper()

@web_app.route("/") #Decorator
def index():
    #render_template is used to return webapges
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/home")
def home():
    if len(session["email"]) != 0:
        return render_template("home.html", store_address= session["store_address"] , name= session["name"], email= session["email"])

    else:
        return redirect("/")
    
@web_app.route("/success")
def success():
    return render_template("success.html", name= session["name"], email= session["email"])

@web_app.route("/error")
def error():
    return render_template("error.html", name= session["name"], email= session["email"])

@web_app.route("/logout")
def logout():
    session["email"] = ""
    session["name"] =  ""
    return redirect("/")


@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    #Create a Dictionary with data from HTML Register Form -> It act as Document
    user_data ={
        "store_code": request.form["store_code"],
        "store_address":request.form["store_address"],
        "GSTIN":request.form["GSTIN"],
        "name": request.form["name"],
        "email": request.form["email"],
        "password":hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on":datetime.datetime.now()
    }

    #Save User in database
    db_helper.collection = db_helper.db["users"]
    result= db_helper.insert(user_data)
    #message = "Welcome to Home Page.User ID is: {}".format(result.inserted_id)
    #return message


    #Write the data in the Session Object
    #This data can now be used anywhere in the project
    session['store_address'] = user_data["store_address"]
    session['name'] = user_data["name"]
    session['email']= user_data["email"]
    
    return render_template("home.html", store_address= session['store_address'] , name= session['name'] , email= session['email'])

@web_app.route("/fetch-user", methods=["POST"])
def fetch_user_from_db():

    #Create a Dictionary with Data from HTML Register Form
    user_data ={
        "email":request.form["email"],
        "password":hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }
    
    db_helper.collection = db_helper.db["users"]
    #Fetch user in Database i.e MongoDB
    result = db_helper.fetch(query=user_data)
    print("result:",result)
    
    if len(result)>0:
        user_data = result[0] #Get the dictionary from List
        session['store_address'] = user_data['store_address']
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]

        return render_template("home.html", store_address= session['store_address'], name = session['name'], email=session['email'])
    
    else:
        return render_template("error.html", message="User not Found.Please Try Again", name= session["name"],email=session["email"])
    

@web_app.route("/add-customer", methods=["POST"])
def add_customer_in_db():
    #Create a Dictionary with data from HTML Register Form -> It act as Document
    customer_data ={
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "address": request.form["address"],
        "manager_email": session["email"],
        "manager_name" : session["name"],
        "created_on":datetime.datetime.now()
    }

    #Save User in database
    db_helper.collection = db_helper.db["customers"]
    #Save patient in Database i.e MongoDb
    result= db_helper.insert(customer_data)
    return render_template("success.html", message = "Customer Added Successfully..", name = session["name"], email = session["email"])

@web_app.route("/update-customer/<id>")
def update_customer(id):
    print("Customer to be updated:", id)
    
    # Save Patient ID in Session, which needs to be updated
    session["id"] = id
    
    # Fetch document from patient collection, where id matches
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["customers"]
    
    # result is a list
    result = db_helper.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with customer id matching the one we have passed
    customer_doc = result[0]

    return render_template("update-customer.html",
                           name=session["name"], 
                           email=session["email"], 
                           customer = customer_doc)


@web_app.route("/delete-customer/<id>")
def delete_customer(id):
    print("Customer to be deleted:", id)
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["customers"]
    db_helper.delete(query)
    return render_template("success.html", message = "Customer Deleted Successfully",
                           name=session["name"], email=session["email"])


@web_app.route("/update-customer-in-db", methods=["POST"])
def update_customer_in_db():

    # Create a Dictionary with Data from HTML Register Form
    customer_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "address": request.form["address"],
        "manager_email": session['email'],
        "manager_name": session['name'],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["customers"]

    query = {"_id": ObjectId(session["id"])}
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.update(customer_data, query)
    return render_template("success.html", message = "Customer Updated Successfully",
                           name=session["name"], email=session["email"])

@web_app.route("/add-sale/<id>")
def add_sale(id):
    # Store the Customer ID in Session, temporarily
    session["customer_id"] = id
    query = {"_id": ObjectId(id)}
    db_helper.collection = db_helper.db["customers"]
    
    # result is a list
    result = db_helper.fetch(query=query)
    
    # As we will get the list of documents, and 0th index will be our document
    # with customer id matching the one we have passed
    customer_doc = result[0]
    session["customer_name"] = customer_doc["name"]
    return render_template("add-sale.html",
                           name=session["name"], email=session["email"],
                           customer_name = session["customer_name"]
                           )


@web_app.route("/add-sale-in-db", methods=["POST"])
def add_sale_in_db():

    # Create a Dictionary with Data from HTML Register Form
    sale_data = {
        "manager_email": session['email'],
        "manager_name": session['name'],
        "customer_id": session["customer_id"],
        "customer_name": session["customer_name"],
        "item _name": request.form["item_name"],
        "item_code": request.form["item_code"],
        "quantity": request.form["quantity"],
        "mrp": request.form["mrp"],
        "net_amount": request.form["net_amount"],
        "coupon_applicable": request.form["coupon_applicable"],
        "retail_offer": request.form["retail_offer"],
        "sold_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["sales"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(sale_data)
    return render_template("success.html", message = "Sale Record Added Successfully",
                           name=session["name"], email=session["email"])





@web_app.route("/fetch-customers")
def fetch_customers_from_db():

    if len(session["email"]) == 0:
        return redirect("/")

    user_data ={
        "manager_email":session["email"],
    }
    
    db_helper.collection = db_helper.db["customers"]
    result = db_helper.fetch(query=user_data)
    #result here is a list of documents(dictionary) from Mongo DB
    

    if len(result)>0:
        print(result)
        return render_template("customers.html", customers = result, 
                               name= session["name"], email=session["email"]) 
    else:
        return render_template("error.html", message="Customers not Found. Please Try Again !",name= session["name"], email=session["email"])
    
@web_app.route("/fetch-sales")
def fetch_sales_from_db():

    if len(session["email"]) == 0:
        return redirect("/")

    user_data ={
        "manager_email":session["email"],
    }
    
    db_helper.collection = db_helper.db["sales"]
    result = db_helper.fetch(query=user_data)
    #result here is a list of documents(dictionary) from Mongo DB
    

    if len(result)>0:
        print(result)
        return render_template("sales.html", sales = result, 
                               name= session["name"], email=session["email"]) 
    else:
        return render_template("error.html", message="Sales not Found. Please Try Again !",name= session["name"], email=session["email"])
    
@web_app.route("/fetch-sales-of-customer/<id>")
def fetch_sales_of_customer_from_db(id):

    if len(session["email"])==0:
        return redirect("/")
    
    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "manager_email": session["email"],
        "customer_id": id
    }

    db_helper.collection = db_helper.db["sales"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("sales.html", sales = result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Sales Not Found. Please Try Again",
                               name=session["name"], email=session["email"])
    
@web_app.route("/search-customer")
def search_customer():
    return render_template("search.html",name= session["name"], email = session["email"])

@web_app.route("/search-customer-from-db", methods=["POST"])
def search_customer_from_db():
    customer_data = {
        "email": request.form["email"],
        "manager_email": session["email"],
    }

    db_helper.collection = db_helper.db["customers"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=customer_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("customer-card.html", customer=result[0], 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Customers Not Found. Please Try Again",
                               name=session["name"], email=session["email"])

def main():
    #In Order to use Session Tracking, create a Secret Key
    web_app.secret_key = "levis-app-key-v1"

    #run will runapp until infinite like while loop , till user won't quit
    web_app.run() #(port number)


if __name__ == "__main__":
    main()
