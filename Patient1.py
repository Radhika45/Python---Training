"""
Doctor's App

User is a Doctor
Doctor should be able to add Patients
Doctor -> User of Application
Patient: pid,name,phone,email,dob,gender,created_on
Consultation : cid, pid,remarks, medicines, next_followup, created_on
"""


"""
create table Patient(
    pid int primary key auto_increment,
    name varchar(256),
    phone varchar(20),
    email varchar(256),
    dob date,
    gender varchar(20),
    created_on datetime  
);
"""

import datetime

class Patient:
    def __init__(self, pid =0, name=" ", phone=" ", email=" ", dob="", gender=" "):
        self.pid = pid
        self.name= name
        self.phone = phone
        self.email= email
        self.dob=dob
        self.gender= gender
        self.created_on= datetime.datetime.now()
    
    def add_patient_details(self):
        self.name = input("Enter Your Name: ")
        self.phone= input("Enter Your Phone: ")
        self.email= input("Enter Your Email: ")
        self.dob = (input("Enter Your DOB (yyyy- mm - dd): "))
        self.gender = input("Enter Your Gender: ")
        #we wil not input created on as is it system date time stamp

    def update_patient_details(self):
        name = input("Enter Your Name: ")
        if len(name) != 0:
            self.name = name

        phone= input("Enter Your Phone: ")
        if len(phone) != 0:
            self.phone = phone

        email= input("Enter Your Email: ")
        if len(email) != 0:
            self.email = email

        dob= input("Enter Your DOB: ")
        if len(dob) != 0:
            self.dob= dob

        gender = input("Enter Your gender: ")
        if len(gender) != 0:
            self.gender = gender
       
        #we wil not input created on as is it system date time stamp


    def show(self):
        print("------------PATIENT--------------")

        patient = """
        {pid} | {name} | {phone}
        {email} | {dob}
        {gender} | {created_on}
        """.format_map(vars(self))
        print(patient)

        print("----------------------------------")