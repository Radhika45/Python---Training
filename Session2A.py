""" Flask

1. pip install Flask

Framework - It is the set of tools used to create other web applications
"""

from flask import *
import datetime
import hashlib
from Session1C import MongoDBHelper

#Create the Object of Flask -> It represents 

web_app = Flask("Doctor's App")
db_helper = MongoDBHelper()

@web_app.route("/") #Decorator
def index():
    
    message = """
    <html>
    <head>
        <tilte>Doctors App</tilte>
    </head>
    <body>
        <center>
            <h3>Welcome to Doctor's App</h3>
            <p>Developed by Radhika</p>
        </center>
            
    </body>
    </html>
    """
    #return message

    #render_template is used to return webapges
    return render_template("index.html")

@web_app.route("/register")
def register():
    return render_template("register.html")

@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    #Create a Dictionary with data from HTML Register Form -> It act as Document
    user_data ={
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
    session['name'] = user_data["name"]
    session['email']= user_data["email"]
    
    return render_template("home.html",name = session['name'] ,email= session['email'])

@web_app.route("/fetch-user", methods=["POST"])
def fetch_user_from_db():

    user_data ={
        "email":request.form["email"],
        "password":hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }
    
    db_helper.collection = db_helper.db["users"]
    result = db_helper.fetch(query=user_data)
    print("result:",result)
    


    if len(result)>0:
        user_data = result[0] #Get the dictionary from List
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]

        return render_template("home.html", name = session['name'],email=session['email'])
    
    else:
        return "User Not Found.Please Try Again"
    

@web_app.route("/add-patient", methods=["POST"])
def add_patient_in_db():
    #Create a Dictionary with data from HTML Register Form -> It act as Document
    patient_data ={
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "age": int(request.form["age"]),
        "address": request.form["address"],
        "doctor_email":session["email"],
        "doctor_name": session["name"],
        "created_on":datetime.datetime.now()
    }

    #Save User in database
    db_helper.collection = db_helper.db["patients"]
    result= db_helper.insert(patient_data)
    message = "Patient Added Successfully.."
    return message


@web_app.route("/fetch-patients")
def fetch_patients_from_db():

    user_data ={
        "doctor_email":session["email"],
    }
    
    db_helper.collection = db_helper.db["patients"]
    result = db_helper.fetch(query=user_data)
    print("result:",result)
    

    if len(result)>0:
        print(result)
        return "Patients Fetched"    
    else:
        return "Patients Not Found.Please Try Again"


def main():
    #In Order to use Session Tracking, create a Secret Key
    web_app.secret_key = "doctors-app-key-v1"

    #run will runapp until infinite like while loop , till user won't quit
    web_app.run() #(port number)



if __name__ =="__main__":
    main()
