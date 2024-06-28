"""
create table Customer(
    cid int primary key auto_increment,
    name varchar(256),
    phone varchar(15),
    email varchar(256),
    age int,
    gender varchar(20),
    created_on datetime
    
)
"""

import datetime

class Customer:
    def __init__(self,cid =0,name=" ",phone=" ",email=" ",age=0,gender=" ",created_on=" "):
        self.cid = cid
        self.name= name
        self.phone = phone
        self.email= email
        self.age= age
        self.gender= gender
        self.created_on= datetime.datetime.now()
    
    def add_customer_details(self):
        self.name = input("Enter Your Name: ")
        self.phone= input("Enter Your Phone: ")
        self.email= input("Enter Your Email: ")
        self.age = int(input("Enter Your Age: "))
        self.gender = input("Enter Your Gender: ")
        #we wil not input created on as is it system date time stamp

    def update_customer_details(self):
        name = input("Enter Your Name: ")
        if len(name) != 0:
            self.name = name

        phone= input("Enter Your Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email= input("Enter Your Email: ")
        if len(email) != 0:
            self.email = email

        age= input("Enter Your Age: ")
        if len(age) != 0:
            self.age= age

        gender = input("Enter Your gender: ")
        if len(gender) != 0:
            self.gender = gender
       
        #we wil not input created on as is it system date time stamp


    def show(self):
        print("------------CUSTOMER--------------")
        print("Customer ID: {}".format(self.cid))
        print("Name: {} |Phone: {} |Email: ".format(self.name, self.phone,self.email))
        print("Age: {} | Gender: {} |Created on:  {}".format( self.age, self.gender,self.created_on))
        print("----------------------------------")